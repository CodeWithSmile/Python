import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
arr1=np.array([1,2,3])
print(arr.shape)
print(arr1.shape)

arr2= np.array([1, 2, 3, 4], ndmin=5)
print(arr2)
print('shape of array :', arr2.shape)