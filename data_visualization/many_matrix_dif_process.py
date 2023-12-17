import csv
import sys
import matplotlib.pyplot as plt
import numpy as np

matrix_info_list = [['null']]
with open('../data/matrix_information.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        matrix_info_list.append(row)

matrix_compute_datas = {}
with open('../compute_data/time.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        key = int(row[0])
        tmp = [row[1], row[2]]
        matrix_compute_datas.setdefault(key, []).append(tmp)

# print(matrix_compute_datas[matrix_cnt])

# show_matrix_ids = [1, 473, 519, 192, 373, 199, 450, 372]
#
# fig, axs = plt.subplots(nrows=2, ncols=4, figsize=(28, 12), dpi=500)
# fig.subplots_adjust(left=0.04, right=0.99, bottom=0.08, top=0.938, wspace=0.255, hspace=0.35)
# cnt = 0
# for matrix_cnt in show_matrix_ids:
#     processes = []
#     times = []
#     for compute_data in matrix_compute_datas[matrix_cnt]:
#         processes.append(compute_data[0])
#         times.append(float(compute_data[1]))
#     min_time = min(times)
#     min_time_index = times.index(min_time)
#     min_process = processes[min_time_index]
#     gflopses = [float(matrix_info_list[matrix_cnt][4]) / (time * 100000) for time in times]
#     axs[cnt // 4, cnt % 4].scatter(processes[:-2], gflopses[:-2], color='#6495ED', s=150)
#     axs[cnt // 4, cnt % 4].scatter(min_process, max(gflopses), color='red', s=200)
#     axs[cnt // 4, cnt % 4].plot(processes[:-2], gflopses[:-2], '-o', color='#6495ED', linewidth=4)
#     axs[cnt // 4, cnt % 4].set_title(matrix_info_list[matrix_cnt][1], fontsize=24)
#     axs[cnt // 4, cnt % 4].set_xlabel('Process Number', fontsize=20)
#     axs[cnt // 4, cnt % 4].set_ylabel('The performance of SpMV/(Gflops)', fontsize=18)
#     axs[cnt // 4, cnt % 4].grid(True)
#     cnt += 1
# # Show the plot
# plt.savefig('many_matrix_dif_process.pdf', format='pdf')

show_matrix_ids = [473, 519,  199, 450]

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(14, 12),dpi=500)
fig.subplots_adjust(left=0.04, right=0.99, bottom=0.08, top=0.938, wspace=0.255, hspace=0.35)
cnt = 0
for matrix_cnt in show_matrix_ids:
    processes = []
    times = []
    for compute_data in matrix_compute_datas[matrix_cnt]:
        processes.append(compute_data[0])
        times.append(float(compute_data[1]))
    min_time = min(times)
    min_time_index = times.index(min_time)
    min_process = processes[min_time_index]
    gflopses = [float(matrix_info_list[matrix_cnt][4]) / (time * 100000) for time in times]
    axs[cnt // 2, cnt % 2].scatter(processes[:-2], gflopses[:-2], color='#6495ED', s=150)
    axs[cnt // 2, cnt % 2].scatter(min_process, max(gflopses), color='red', s=200)
    axs[cnt // 2, cnt % 2].plot(processes[:-2], gflopses[:-2], '-o', color='#6495ED', linewidth=5)
    axs[cnt // 2, cnt % 2].set_title(matrix_info_list[matrix_cnt][1], fontsize=25)
    axs[cnt // 2, cnt % 2].set_xlabel('Process Number', fontsize=20)
    axs[cnt // 2, cnt % 2].set_ylabel('The performance of SpMV/(Gflops)', fontsize=20)
    axs[cnt // 2, cnt % 2].grid(True)
    cnt += 1
plt.tight_layout()
plt.savefig('many_matrix_dif_process_4.pdf', format='pdf')