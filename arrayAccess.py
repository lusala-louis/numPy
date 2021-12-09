import numpy as np
array1=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(array1)
print(' ')
#Get a specific element [r,c]
print(array1[1,5])
print(' ')
#Get a specific row
print(array1[0, : ])
print(' ')
#Get a specific column
print(array1[: , 2 ])
print(' ')
#stepping through a row[startindex:stopindex:stepindex]
print(array1[0,1:6:2])
print(' ')
#Changing an element
array1[1,5]=20
print(array1)
print(' ')
#Changing a series of elements in a column
array1[:,2]=5
print(array1)
print(' ')
array1[:,2]=[2,5]
print(array1)
print(' ')
#Working on a 3d array
array2=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(array2)
print(' ')
array2[0,1,1]=6  #Changing the '4' in [3,4] to '6'
print(array2)
print(' ')
print(array2[:,0,:])   #Getting the elements in the first rows of the two matrices