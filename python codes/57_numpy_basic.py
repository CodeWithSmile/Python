import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
arr1=np.array((1,2,3))
print(arr1)
#array dimension
# 1)0-d array
arra1=np.array(45)
print(arra1)
print("dimension",arra1.ndim)
# 1-d array
arra2=np.array([1,2])
print(arra2)
print("dimension",arra2.ndim)
# 2-rd array
arra3=np.array([[1,2],[3,4]])
print(arra3)
print("dimension",arra3.ndim)
#3d array
arra4=np.array([[[1,2],[3,4],[5,6]]]) #([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arra4)
print("dimension",arra4.ndim)
#check higher dimension
arr2 = np.array([1, 2, 3, 4], ndmin=5)
print(arr2)
print('number of dimensions :', arr2.ndim)