## 机器学习大作业

### 题目
A Machine Learning-Based Model for Automated Selection of Task Granularity in Sparse Matrix-Vector Multiplication (SpMV) Operations

### 摘要

In this study, we conducted an in-depth discussion on the task granularity selection for Sparse Matrix-Vector Multiplication(SpMV kernel).Initially, we thoroughly analyzed the specific impact of different task granularities on performance in SpMV operations. Experimental observations revealed that varying task granularities significantly affect the computational performance of SpMV when processing certan sparse matrices. Furthermore, the research indicated that there is no universal task granularity setting that can adapt to the optimal performance needs of all SpMV kernels.

Based on this finding, we proposed a supervised learning-based method to select the optimal task granularity for SpMV. The training process of this model involved extracting features from sparse matrices to describe the characteristics of the input datasets. Additionally, we utilized optimal task granularity data from thousands of SpMV kernels executed on supercomputers for the model’s supervised learning. This process ultimately produced a highly accurate prediction model.

The experimental results showed that, compared to traditional fixed task assignment methods, using our model to choose the appropriate task granularity for a specific sparsematrix can achieve a performance improvement of about 20%. This accomplishment not only demonstrates the potential of machine learning in optimizing high-performance computing tasks but also provides a new perspective for performance optimization of SpMV kernels.
