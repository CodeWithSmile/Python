import numpy as np
#1-d to 2-d array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
print(newarr.ndim)

# 1-d to 3-d
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

#unknown dimension
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

#flattening array
arr=np.array([[1, 2, 3], [4, 5, 6]])
newarr=arr.reshape(-1)
print(newarr)