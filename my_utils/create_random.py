import random

random.seed(42)


# 生成随机的乘法向量
def create_vector_x(mtx_n):
    vector_x = [random.randint(1, 10) for _ in range(mtx_n)]
    return vector_x


# 为矩阵类型为patten的矩阵生成随机非零值
def create_csr_value(nnz):
    csr_value = [random.uniform(-100.00, 100) for _ in range(nnz)]
    return csr_value
