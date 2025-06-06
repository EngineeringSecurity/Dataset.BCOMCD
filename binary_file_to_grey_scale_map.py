import os
from PIL import Image

input_folder_path = 'file_input_output/AES128/AES128_same_key2/Randomimage_bin_AES128_ECB'

# 生成输出路径
output_folder_path = os.path.join(
    os.path.dirname(input_folder_path),
    os.path.basename(os.path.normpath(input_folder_path)) + '_grey_map_512x512'
)

# 确保输出目录存在
os.makedirs(output_folder_path, exist_ok=True)

# 目标尺寸
desired_width, desired_height = 512,512
total_pixels = desired_width * desired_height

for filename in os.listdir(input_folder_path):
    if filename.endswith((".bin", ".enc")):
        filepath = os.path.join(input_folder_path, filename)

        with open(filepath, 'rb') as f:
            binary_data = f.read()

        # 处理数据长度不足
        if (data_len := len(binary_data)) < total_pixels:
            print(f"扩展文件: {filename} (原始长度 {data_len})")

            if data_len == 0:
                raise ValueError("文件内容为空，无法扩展")

            # 计算需要复制的次数（向上取整）
            times_needed = (total_pixels + data_len - 1) // data_len
            binary_data = binary_data * times_needed  # 一次性复制
            print(f"扩展后长度: {len(binary_data)}")

        # 截断至目标长度
        binary_data = binary_data[:total_pixels]

        # 生成灰度图
        img = Image.new('L', (desired_width, desired_height))
        img.putdata(list(binary_data))

        # 保存并验证
        output_path = os.path.join(output_folder_path, f"{os.path.splitext(filename)[0]}_key2_gray.png")
        img.save(output_path)
        assert Image.open(output_path).mode == 'L', "通道模式验证失败"

        print(f"已生成: {output_path}")