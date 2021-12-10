import numpy as np
#Parsing data from a file
filedata=np.genfromtxt('data.txt', delimiter=',')
print (filedata)
print(' ')
print(filedata.astype('int32'))
print(' ')
#Boolean masking and advanced indexing
#Shows True or False whether the given item in filedata is greater than 50
print(filedata>50)  
print(' ')
#Grab only the items in filedata that are greter than 50
print(filedata[filedata>50])
#Show if any of the data in a column are greter than 50
print(np.any(filedata>50,axis=0))
print(' ')
#Show columns where all the data are greter than 50
print(np.all(filedata>50,axis=0))
print(' ')