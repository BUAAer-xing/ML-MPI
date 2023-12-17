import csv


def out_file(file_name, data, type):
    if type == 'txt':
        with open(file_name, 'a') as file:
            # 写入文本
            file.write(data)
    elif type == 'csv':
        with open(file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            # 遍历结果列表并写入
            writer.writerow(data)
