import numpy as np

arr = np.array([1,2,3,4,5,6])

new_arr = np.insert(arr,6,7,axis=None)
print(new_arr)


mull_arr = np.array([
    [1,2,3],
    [4,5,6]
])

new_arr_mul = np.insert(mull_arr, 3,7,axis=0)
print(new_arr_mul)