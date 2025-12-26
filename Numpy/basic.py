import numpy as np

array1 = [1,2,3,4,5]
print(array1)

#numpy array
arr_1 = np.array(array1)
print(arr_1)


#Creating arr to numpy arrr

arr_2 = np.array([1,2,3,4,5,6,7])
print(arr_2)

#Creating zeros numpy array
arr_3 = np.zeros((3,2))
print(arr_3)

#Creating ones numpy array
arr_4 = np.ones((1,2))
print(arr_4)

#Ceating array of specific number using full function(syntax: np.full(shape,value))

arr_5 = np.full((2,5), 6)
print(arr_5)

#Creating sequence of numbers array in numpy
arr_6 = np.arange(10,20,2)
print(arr_6)

#Creating identity matrices
arr_7 = np.eye(4)
print(arr_7)