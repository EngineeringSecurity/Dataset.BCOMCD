import cv2
import numpy as np
import os

print(cv2.__version__)

# 指定输入文件夹路径
input_folder = r'file_input_output\AES128_same_key2\dataset_AES128_same_key2\dataset_AES128_same_key2_512x512_HistEq\Randomimage_bin_AES128_OFB_grey_map_512x512'

# 指定输出文件夹路径，根据输入文件夹名生成
output_folder = f'{input_folder}_HistEq'

# 如果输出文件夹不存在，则创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    # 检查文件是否为图像
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff')):
        # 构建完整的文件路径
        file_path = os.path.join(input_folder, filename)
        # 读取图像（灰度模式）
        img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(12, 12))

        # 应用CLAHE
        enhanced_img = clahe.apply(img)

        # 构建输出文件路径
        output_file_path = os.path.join(output_folder, filename)

        # 保存增强后的图像
        cv2.imwrite(output_file_path, enhanced_img)

# 所有图像处理完成
print(f'All images have been processed and saved to {output_folder}')
