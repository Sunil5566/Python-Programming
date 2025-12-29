import numpy as np

arr = np.array([1,2,3,4,5,6])

arr_1 = arr.reshape(2,3)
print(arr_1) #it convert 1 d to 2 d array

#flatten
arr_2 = np.array ([
    [1,2,3],
    [4,5,6]
])

arr_3 = (arr_2.flatten())  
print(arr_3)


#Ravel()  
arr_4 = (arr_2.ravel())
print(arr_4)
#ravel()

#Note : .....ravel changes in original array, but flatten returns its copy


