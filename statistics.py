import numpy as np
stats=np.array([[1,2,3],[4,5,6]])
print(stats)
print(' ')
#Minimum item in array
stats_minimum=np.min(stats)
print(stats_minimum)
print(' ')
stats_minimum=np.min(stats,axis=0)  #Minimum values along the columns
print(stats_minimum)
print(' ')
#Maximum item in array
stats_maximum=np.max(stats)
print(stats_maximum)
print(' ')
stats_maximum=np.max(stats, axis=1)  #Maximum values along the rows
print(stats_maximum)
print(' ')
#Sum of all elements in the array
total=np.sum(stats)
print(total)
print(' ')
row_total=np.sum(stats,axis=1) #Sum of elements along the rows
print(row_total)
print(' ')