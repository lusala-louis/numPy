import numpy as np

#Creating a 3*3 array with all zeros
array1=np.zeros((3,3))
print(array1)
print(' ')

#Creating a 2*2 array of all ones
array2=np.ones((2,2))
print(array2)
print(' ')

#Creating a 3*3 constant array
array3=np.full((3,3),7)
print(array3)
print(' ')

#Creating a 3*3 array filled with random values
array4=np.random.random((3,3))
print(array4)
print(' ')

#Creating a 3*3 identity matrix
identityMatrix=np.eye(3)
print(identityMatrix)
print(' ')