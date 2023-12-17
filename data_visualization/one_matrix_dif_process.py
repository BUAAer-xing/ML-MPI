import csv
import sys
import matplotlib.pyplot as plt
import numpy as np

# 检查是否有足够的参数传递给程序
if len(sys.argv) > 1:
    # 设置每次进行运行的矩阵的参数
    matrix_cnt = int(sys.argv[1])
else:
    matrix_cnt = 1

matrix_info_list = [['null']]
with open('../data/matrix_information.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        matrix_info_list.append(row)

print("矩阵的基本情况为：", matrix_info_list[matrix_cnt])

matrix_compute_datas = {}
with open('../compute_data/time.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        key = int(row[0])
        tmp = [row[1], row[2]]
        matrix_compute_datas.setdefault(key, []).append(tmp)

# print(matrix_compute_datas[matrix_cnt])

processes = []
times = []
for compute_data in matrix_compute_datas[matrix_cnt]:
    processes.append(compute_data[0])
    times.append(float(compute_data[1]))

min_time = min(times)
min_time_index = times.index(min_time)
min_process = processes[min_time_index]
gflopses = [float(matrix_info_list[matrix_cnt][4]) / (time*100000) for time in times]


# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(processes, gflopses, color='green')
plt.scatter(min_process, max(gflopses), color='red', s=150)
plt.plot(processes, gflopses, '-x', color='green')  # Connecting the dots with a line

# Adding titles and labels
plt.title('One Matrix Different Processes', fontsize='20')
plt.xlabel('Process Number', fontsize='16')
plt.ylabel('The performance of SpMV/(Gflops)', fontsize='16')

# Show the plot
plt.show()



