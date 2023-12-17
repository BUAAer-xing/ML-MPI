import random

import numpy as np
import scipy.io as sio
import csv
import scipy.sparse as ssp

random.seed(42)


def create_csr_value(nnz):
    csr_value = [random.uniform(-100.00, 100) for _ in range(nnz)]
    return csr_value


matrix_name_list = ['null']
with open('matrix_information.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        matrix_name_list.append(row[1])

#  最大的ID为1628
csv_rows = []
for matrix_name in matrix_name_list[1:]:
    file_path = "../downloaded_matrix/" + matrix_name + '/' + matrix_name + '.mtx'  # 相对路径
    mtx = sio.mmread(file_path)  # 读入mtx格式的矩阵数据
    info = sio.mminfo(file_path)  # 获取读入的矩阵信息
    if info[3] == 'pattern':  # 如果没有填充数，则随机生成后再进行填充
        nnz_value = create_csr_value(len(mtx.data))
        mtx.data[:] = nnz_value
    mtx_m = info[0]  # 行数
    mtx_n = info[1]  # 列数
    nnz = info[2]  # 非零元数
    nnz_frac = nnz / float(mtx_m * mtx_n) * 100  # 非零元素的占比
    min_value = min(mtx.data)  # 非零元的最小值
    max_value = max(mtx.data)  # 非零元的最大值
    csr_matrix = ssp.csr_matrix(mtx)
    nz_p_row = np.diff(csr_matrix.indptr)
    avg_nz_p_row = np.mean(nz_p_row)  # 平均每行的非零元的个数
    std_nz_p_row = np.std(nz_p_row)  # 平均每行的非零元个数的标准差
    csv_rows.append([matrix_name, mtx_m, mtx_n, nnz_frac, float(min_value), float(max_value), avg_nz_p_row, std_nz_p_row])

with open('matrix_features.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['matrix_name', 'n_rows', 'n_cols', 'nnz_frac', 'min_value', 'max_value', 'avg_nz_p_row',
                     'std_nz_p_row'])
    for row in csv_rows:
        writer.writerow(row)
