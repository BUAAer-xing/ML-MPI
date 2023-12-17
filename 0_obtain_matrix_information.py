import ssgetpy
import csv

filename = 'data/matrix_information.csv'

result = ssgetpy.search(nzbounds=(0, 100000), limit=3000)  # 默认限制为10,更改为所有的矩阵

with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'rows', 'cols', 'nnz'])
    for matrix in result:
        row = [matrix.id, str(matrix.name), matrix.rows, matrix.cols, matrix.nnz]
        writer.writerow(row)