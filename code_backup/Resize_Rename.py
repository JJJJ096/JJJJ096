from PIL import Image
import os

def rename(file_path, label):
    import os
    file_names = os.listdir(file_path)
    idx = 1
    for name in file_names:
        src = os.path.join(file_path, name)
        dst = str(label) + str(idx) + '.jpg'
        dst = os.path.join(file_path, dst)
        os.rename(src, dst)
        idx += 1
    return print("complete")

def resize(file_path, size):
    file_names = os.listdir(file_path)
    idx = 1
    for name in file_names:
        img_name = file_path + '/' + name
        img = Image.open(img_name)
        img_resize= img.resize(size, Image.LANCZOS)
        img_resize.save('C:/Users/KAMIC/Desktop/meltpool/Melt_Pool/melt_pool_{}.png'.format(idx))
        idx += 1
    return print("complete")


if __name__ == '__main__':
    rename('C:/Users/KAMIC/Desktop/original_data/spatter/', 'Spatter_')
    # resize('C:/Users/KAMIC/Desktop/original_data/melt_pool', (224,224))