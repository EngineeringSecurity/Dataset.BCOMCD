import os
from PIL import Image

# 设置原始图片文件夹路径和输出文件夹路径
input_folder = r'P:\Password_working_modle_recognition\picture_folder_to_binary\file_input_output\Randomimage'
output_folder = input_folder + '_bin_files'  # 输出文件夹

# 检查输入文件夹是否存在
if not os.path.exists(input_folder):
    print(f"错误：输入文件夹 '{input_folder}' 不存在。")
    print("请确保文件夹路径正确，并且文件夹已创建。")
    exit(1)

# 创建输出文件夹（如果不存在）
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有图片
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert('L')  # 强制转换为灰度图
        binary_data = img.tobytes()  # 将灰度图转换为二进制数据

        # 保存为二进制文件
        output_filename = os.path.splitext(filename)[0] + '.bin'  # 生成对应的 .bin 文件名
        output_path = os.path.join(output_folder, output_filename)
        with open(output_path, 'wb') as f:
            f.write(binary_data)

        print(f"已处理 {filename}，生成 {output_filename}")

print("处理完成。")