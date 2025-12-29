import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

print(np.split(arr1,2))

print(np.vstack((arr1,arr2))) #row wise
print(np.hstack((arr1,arr2)))  #column wise
