import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr1= np.array(['apple', 'banana', 'cherry'])
print(arr1.dtype)

arr2 = np.array([1, 2, 3, 4], dtype='S')
print(arr2)
print(arr2.dtype)

arr3= np.array([1, 2, 3, 4], dtype='i4')
print(arr3)
print(arr3.dtype)

arr4 = np.array([1.1, 2.1, 3.1])
newarr = arr4.astype('i')
print(newarr)
print(newarr.dtype)

arr5=np.array(('a','b','c'))
narr=arr5.astype('i')
print(narr)
print(narr.dtype)