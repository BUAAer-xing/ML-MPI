
# spmv 计算函数
def spmv_mpi(matrix, vector, start, end):
    val = matrix.data
    col_idx = matrix.indices  # 列索引
    row_offset = matrix.indptr  # 压缩的行索引
    ans = []
    for i in range(start, end):
        tmp_sum = 0
        for j in range(row_offset[i], row_offset[i + 1]):
            tmp_sum += val[j] * vector[col_idx[j]]
        ans.append(tmp_sum)
    return ans