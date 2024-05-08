import pydicom
import numpy as np

def load_dicom(filename):
    # 读取DICOM文件
    ds = pydicom.dcmread(filename)
    # 将像素数据转换为numpy数组
    image = ds.pixel_array
    print("Loaded DICOM file:", filename)
    print("Image dimensions:", image.shape)
    return image

# 例子：加载DICOM文件
dicom_image = load_dicom('path_to_dicom_file.dcm')
