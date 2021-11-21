from numpy.core.fromnumeric import shape
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tkinter import filedialog as fd
from math import ceil

def Data_load(): # data 불러오는 함수

    file_name = fd.askopenfilename(initialdir='C:/User',
                                    title="file", filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    data = pd.read_csv(file_name, header=None, names=['date', 'num', 'x','y','z','c','a','vol','T'])
    data = data[['x','y','z','c','a','T']]
    data = data.query('T >= 1500')
    # data = data.query('0<=z<10')
    #data = data.reset_index()
    print(data)
    return data

# 5축 데이터를 3축으로 변환하는 함수
def data_transform(x,y,z,c,a):
    pi = np.pi
    c_rad = c / 180 * pi
    a_rad = a / 180 * pi
    xx = x * np.cos(c_rad) * np.cos(a_rad) - y * np.sin(c_rad) + z * np.cos(c_rad) * np.sin(a_rad)
    yy = x * np.sin(c_rad) * np.cos(a_rad) + y * np.cos(c_rad) + z * np.sin(c_rad) * np.sin(a_rad)
    zz = - x * np.sin(a_rad) + z * np.cos(a_rad)
    return xx, yy, zz

def layer_temp(data, layer_thickness):
    
    layer_temp_mean = []
    layer_temp_max = []
    layer_list = np.arange(0, max(data['z']), layer_thickness)

    for z in layer_list:
        layer_temp = data.query('z=={}'.format(z))
        layer_mean = np.mean(layer_temp['T'])
        layer_max = np.max(layer_temp['T'])
        layer_temp_mean.append(round(layer_mean, 2))
        layer_temp_max.append(round(layer_max,2))
    return layer_temp_mean, layer_temp_max

# 3축으로 변환 된 좌표, 온도데이터를 이용하여 3차원 Plot을 그린다.
def plot_3D(x,y,z,t):
    fig = plt.figure(figsize=(12,10))
    ax = plt.gca(projection='3d')
    sctt = ax.scatter(x, y, z, alpha=1, c=t, cmap='jet', s=3, vmin=min(t), vmax=max(t), lw=0)
    plt.title("Melt Pool Temperature")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    #ax.grid(False)
    #ax.set_axis_off()
    # ax.set_frame_on(True)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_zlim(0, max(z))
    fig.colorbar(sctt, ax=ax, shrink=0.7, aspect=10)
    ax.view_init(20, 90)                                        # 그래프 각도 view_init(z축, x-y축)
    plt.tight_layout()
    plt.show()

def meshgrid(x,y,z,t):
    
    fig = plt.figure(figsize=(12,10))
    ax = plt.gca(projection='3d')
    
    sctt = ax.scatter(x, y, z, alpha=1, c=t, cmap='jet', s=50, vmin=min(t), vmax=max(t),lw=0)
    plt.title("Melt Pool Temperature")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    #ax.grid(False)
    #ax.set_axis_off()

    ax.set_xlim(min(x), max(x))
    ax.set_ylim(min(y), max(y))
    ax.set_zlim(min(z), max(z))
    fig.colorbar(sctt, ax=ax, shrink=0.7, aspect=10)
    ax.view_init(0, 90)                                        # 그래프 각도 view_init(z축, x-y축)
    plt.tight_layout()
    plt.show()

def plot_2d(t):

    fig = plt.figure(figsize=(12,8))
    
    #plt.plot(t.index/33, t, color='r', linewidth='0.1')
    plt.scatter(t.index/33, t, color='r', s=0.2)
    #plt.scatter(t.index/33, t, s=1)
    plt.xlabel('time(s)')
    plt.ylabel('Temperature')
    
    # plt.xticks(time)

    plt.tight_layout()
    plt.show()

def layer_bar(data):
    layer_temp_mean, layer_temp_max = layer_temp(data, 0.25)

    width = np.arange(0, max(data['z']),0.25)
    # width = width.tolist()
    layer_temp_mean = np.asarray(layer_temp_mean)
    layer_temp_max = np.asarray(layer_temp_max)

    xerr = layer_temp_max-layer_temp_mean
    yerr = np.zeros(len(xerr))
    error = [yerr,xerr]
    print(shape(error))
    fig = plt.figure(figsize=(12, 10))

    plt.barh(width, layer_temp_mean, height=0.1, color='r')
    # , xerr=error, capsize=2, linewidth=0.1)
    plt.xlabel("temperature")
    plt.ylabel("layer(mm)")
    plt.xlim(1200, max(layer_temp_max))
    plt.title("melt pool temperature per layer")
    plt.show()

def main():
    data = Data_load()
    
    x, y, z, c, a, t = data['x'], data['y'], data['z'], data['c'], data['a'], data['T']

    #xx, yy, zz = data_transform(x,y,z,c,a)    
    #fig = plt.figure(figsize=(16,9))
    #plt.plot(data['T'], 'r', linewidth=0.5)
    #plot_3D(x, y, z, t)
    # plot_2d(t)
    # meshgrid(x,y,z,t)
    layer_bar(data)

if __name__ == '__main__':
    main()