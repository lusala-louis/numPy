import numpy as np
array1=np.full((2,3),7)
print(array1)
print(' ')
array2=np.full((3,2),4)
print(array2)
print(' ')
#Multiplication
product=np.matmul(array1,array2)
print(product)
print(' ')
#Determinant
identity=np.identity(3)
determinant=np.linalg.det(identity)
print(determinant)
print(' ')
