import csv

from matplotlib import pyplot as plt

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

times = []
min_times = []
min_processes = []
for i in range(1, len(matrix_info_list)):
    matrix_compute_data = matrix_compute_datas[i]
    for processes_data in matrix_compute_data:
        times.append(processes_data[1])
    min_times.append(min(times))
    min_index = times.index(min(times))
    min_processes.append(matrix_compute_data[min_index][0])
    times.clear()

with open('process_min_time.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['matrix_cnt', 'min_processes', 'min_times'])
    for i in range(1, len(matrix_info_list)):
        writer.writerow([i, min_processes[i-1], min_times[i-1]])

tong_ji = {}
for min_process in min_processes:
    if min_process not in tong_ji:
        tong_ji[min_process] = 0
    tong_ji[min_process] += 1


processes = sorted(tong_ji, key=lambda x: int(x))
number = [tong_ji[key] for key in processes]

plt.figure(figsize=(10, 6), dpi=500)
bars = plt.bar(processes, number, color='skyblue', align='center', width=0.8)

# plt.title('The Number of Max Gflops Processes', fontsize=25)
plt.xlabel('Number of Process', fontsize=25)
plt.ylabel('Number', fontsize=25)

for bar in bars:
    y_val = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, y_val, y_val, ha='center', va='bottom', fontsize=15)
plt.tight_layout()
plt.savefig('min_time.pdf', format='pdf')
plt.show()
