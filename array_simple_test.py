import numpy as np
array=np.ones((5,5))
print(array)
print(' ')
zeroArray=np.zeros((3,3))
print(zeroArray)
print(' ')
zeroArray[1,1]=9
print(zeroArray)
print(' ')
array[1:4,1:4]=zeroArray
print(array)