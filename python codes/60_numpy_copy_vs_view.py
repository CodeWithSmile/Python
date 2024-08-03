import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.copy()
x[0]=11
print(x)
print(arr)
#view made changes in original array
arr1=np.array([11,22,33,44])
x1=arr1.view()
x1[0]=88
print(x1)
print(arr1)
print(x.base)
print(x1.base)