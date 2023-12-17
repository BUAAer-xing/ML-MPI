import os
import csv

folder_path = 'downloaded_matrix'
csv_file_path = 'data/matrix_information.csv'
file_names = os.listdir(folder_path)

csv_file_names = []

with open(csv_file_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for row in csv_reader:
        csv_file_names.append(row[1])
cnt = 0

tmp = {}

for csv_file_name in csv_file_names:
    flag = 0
    if csv_file_name not in tmp:
        tmp[csv_file_name] = 0
    tmp[csv_file_name] += 1
    if tmp[csv_file_name] > 1:
        print(csv_file_name)
    if csv_file_name+".tar.gz" in file_names:
        flag = 1
        cnt += 1
    if flag == 0:
        print(csv_file_name)

print(cnt)

for file_name in file_names:
    flag = 0
    for csv_file_name in csv_file_names:
        if file_name[:-7] == csv_file_name:
            flag = 1
    if flag == 0:
        print(file_name)

print(len(file_names))
