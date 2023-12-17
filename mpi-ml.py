import time
from mpi4py import MPI
from spmv_mpi import spmv_mpi
import scipy.io as sio
import scipy.sparse as ssp
import csv
import sys
from my_utils import create_random
from my_utils.outfile import out_file

# 检查是否有足够的参数传递给程序
if len(sys.argv) > 1:
    # 设置每次进行运行的矩阵的参数
    matrix_id = int(sys.argv[1])
    log_file = sys.argv[2]
    time_file = sys.argv[3]
else:
    matrix_id = 1

matrix_name_list = ['null']
with open('data/matrix_information.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        matrix_name_list.append(row[1])

#  最大的ID为1628
file_path = "downloaded_matrix/" + matrix_name_list[matrix_id] + '/' + matrix_name_list[matrix_id] + '.mtx'  # 相对路径
mtx = sio.mmread(file_path)  # 读入mtx格式的矩阵数据
info = sio.mminfo(file_path)  # 获取读入的矩阵信息
mtx_m = info[0]
mtx_n = info[1]

if info[3] == 'pattern':  # 如果没有填充数，则随机生成后再进行填充 !!!!!!其实这个地方如果要进行填充的话，应该为4
    nnz_value = create_random.create_csr_value(len(mtx.data))
    mtx.data[:] = nnz_value

csr_mtx = ssp.csr_matrix(mtx)  # 转化为csr矩阵

# 生成乘法向量x，x由随机数组成
x_vector = create_random.create_vector_x(mtx_n=info[1])

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
k = mtx_m // size

start = time.time()
if rank == size - 1:
    local_ans = spmv_mpi(csr_mtx, x_vector, rank * k, mtx_m)
else:
    local_ans = spmv_mpi(csr_mtx, x_vector, rank * k, (rank + 1) * k)
spmv_ans = comm.gather(local_ans, root=0)
end = time.time()
local_time = end - start
sum_time = comm.gather(local_time, root=0)
# print("rank",rank,"times",local_time,"s")
percent_time = "rank: " + str(rank) + "  times: " + str(local_time) + "s" + '\n'
out_file(log_file, percent_time, type='txt')

if rank == 0:
    # 应该选取子进程最长的时间作为乘法的时间，而不是所有子进程的时间求和，因为每个子进程之间是并行执行的
    start_0 = time.time()
    total_ans = []
    for e in spmv_ans:
        for ee in e:
            total_ans.append(ee)
    end_0 = time.time()
    max_time = "稀疏矩阵的ID为 "+str(matrix_id)+" 且进程数为 " + str(size) + " 时，程序所需要的执行时间为：" + str(
        max(sum_time) + end_0 - start_0) + " s \n\n\n"
    out_file(log_file, max_time, type='txt')
    message = [matrix_id, size, max(sum_time) + end_0 - start_0]
    out_file(time_file, message, type='csv')
