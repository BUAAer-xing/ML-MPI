import tarfile
import os

# 获取当前文件夹的路径
current_folder = 'downloaded_matrix'
cnt = 0
# 遍历当前文件夹中的所有文件
for file_name in os.listdir(current_folder):
    # 检查文件是否是.tar.gz文件
    if file_name.endswith('.tar.gz'):
        # 构建完整的文件路径
        file_path = os.path.join(current_folder, file_name)
        # 打开.tar.gz文件
        print(file_name)
        with tarfile.open(file_path, 'r:gz') as tar:
            # 解压到当前文件夹
            tar.extractall(path=current_folder)
        print(f'Extracted {file_name}')
        cnt += 1
        print("Extracting...", cnt)
