# TDMS File Handling Code
# Read TDMS, Synchronization, Interpolation

# TdmsFile.read(file_path)
# group = file['group_name']
# channel = group['channel_name'] or channel = tdms_file['group']['channel']
# time = channel.time_track().seconds
# channel.time_track(absolute_time = Ture)
# time을 기준으로 Synchroization,  HOW?
# data.interpolate(mathod='values') : x_axis, y_axis
# z_axis : Nan 채우기, HOW?  -> fillna(method = 'pad' and 'ffill')  fillna(method='bfill'or 'backfill') 데이터를 채우는 방향
# timestamp 2-64 seconds의 정밀도를 가짐
from nptdms import TdmsFile
import numpy as np
import pandas as pd
from scipy import interpolate
import datetime

def Tdms_processing():
    file_name = "E:/2021생기원/02.Monitoring/00.Labview 코드 개발/TDMS data/DED_monitoring.tdms"
    with TdmsFile.read(file_name, raw_timestamps=True) as tdms_file:
        tdms_file = TdmsFile.read(file_name, raw_timestamps=True)

        mpt = tdms_file['DAQ']['Melt pool temp']
        lp = tdms_file['DAQ']['Laser power']
        x_axis = tdms_file['Position']['x axis']
        y_axis = tdms_file['Position']['y axis']
        z_axis = tdms_file['Position']['z axis']
        c_axis = tdms_file['Position']['c axis']
        a_axis = tdms_file['Position']['a axis']

    time_daq = mpt.properties['wf_start_time'].seconds + mpt.time_track()
    time_position = x_axis.properties['wf_start_time'].seconds + x_axis.time_track()

    # DAQ_time = mpt.time_track(absolute_time=True)
    DAQ_df = pd.DataFrame(data={'time':time_daq,
                                "melt pool temp":mpt, 
                                "laser power":lp})
        
    # position_time = x_axis.time_track(absolute_time=True)
    position_df = pd.DataFrame(data={'time':time_position, 
                                'x':x_axis, 
                                'y':y_axis, 
                                'z':z_axis, 
                                'c':c_axis, 
                                'a':a_axis})
    data = pd.merge(DAQ_df, position_df, how='outer',on='time')
                                                            #, indicator=True) # time을 기준으로 데이터를 합침
    #data = data.interpolate(method='values') # imterpolation
    # fillna(method = 'pad' and 'ffill')  fillna(method='bfill'or 'backfill') 데이터를 채우는 방향
    data['x'] = data['x'].interpolate(method='values')
    data['y'] = data['x'].interpolate(method='values')
    data['z'] = data['z'].fillna(method='ffill')
    data['c'] = data['c'].interpolate(method='values')
    data['a'] = data['a'].fillna(method='ffill')
    # print(data)
    # data.to_csv("test.csv")
    return data

def TDMS_plot_3d(data):
    