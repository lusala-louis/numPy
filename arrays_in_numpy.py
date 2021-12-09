import numpy as np

#Initializing a 3*3 array with all zeros
array1=np.zeros((3,3))
print(array1)
print(' ')

#Initializing a 2*2 array of all ones
array2=np.ones((2,2))
print(array2)
print(' ')

#Initializing a constant array of any number np.array((shape of the array),number you want to fill array with)
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

#Converting a list into an array
array5=np.array([3,2,1,0])
print(array5)
print(' ')

# arange() will create arrays with regularly incrementing values
array6=np.arange(10)
print(array6)
print(' ')

# Create an array of given range with specific data type
array7= np.arange(1, 8, dtype=np.float64)
print (array7)
print(' ')
array8= np.arange(1, 8,dtype=np.int64)
print(array8)
print(' ')
array9= np.arange(1, 8, 0.1,dtype=np.float64)
print (array9)
print(' ')

# linspace() will create arrays with a specified number of items which are spaced equally between the specified beginning and end values
array10=np.linspace(2.0,4.0,5)
print(array10)
print(' ')