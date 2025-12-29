import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

array_3 = np.concatenate((arr1,arr2), axis=0)
print(array_3)