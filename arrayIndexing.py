#Integer array indexing
import numpy as np
a=np.array([[1,2],[3,4]])
print(a)
#Getting the dimension of an array
print(a.ndim)
#Get the shape of the array
print(a.shape)
#Get the datatype of the array
print(a.dtype)
#Get the size of the array
print(a.itemsize)
#Get the number of items in  the array
print(a.size)
#Get the size of the array
print(a.size*a.itemsize)
print(a.nbytes)
print(a[[0,1],[0,1]])