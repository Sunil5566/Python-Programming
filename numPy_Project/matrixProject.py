import numpy as np

Matrix_A = np.array([[1,2,3],
                     [4,5,6],
                     [7,8,9]])
Matrix_B = np.array([[9,8,7],
                     [6,5,4],
                     [3,2,1]])

#addition
add = Matrix_A + Matrix_B
print(add)

#subtraction
sub = Matrix_A - Matrix_B
print(sub)

#multiplication
mut = Matrix_A * Matrix_B
print(mut)

#matrix multiplication or dot product
matrix_mult = np.dot(Matrix_A, Matrix_B)
print(matrix_mult)

#Transpose

Transpose_A = np.transpose(Matrix_A)
print("The transpose of Matrix A is \n" , Transpose_A)

Detr_A = np.linalg.det(Matrix_A)
print(Detr_A)

