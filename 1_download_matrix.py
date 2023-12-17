import ssgetpy
from mpi4py import MPI

filename = 'data/matrix_information.csv'
path = 'downloaded_matrix'

n = 1636  # 最大数量
result = ssgetpy.search(nzbounds=(0, 100000), limit=3000)  # 默认限制为10,更改为所有的矩阵
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
k = n // size
if rank == size - 1:
    for matrix in result[rank * k:n]:
        matrix.download(format='MM', destpath=path)
else:
    for matrix in result[rank * k:(rank + 1) * k]:
        matrix.download(format='MM', destpath=path)
