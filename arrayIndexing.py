#Integer array indexing
import numpy as np
a=np.array([[1,2],[3,4]])
print(a)
print(a[[0,1],[0,1]])
#Getting the dimension of an array
print(a.ndim)
#Get the shape of the array
print(a.shape)
#Get the datatype of the array
print(a.dtype)
b=np.array([[1,3],[3,5]])
print(np.array([b[0,1],b[1,1]]))
