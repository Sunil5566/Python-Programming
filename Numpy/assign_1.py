#Indexin slicing and filtering

import numpy as np

data = np.array([
 [45, 78, 88, 90, 1],
 [67, 55, 72, 60, 0],
 [90, 92, 85, 88, 1],
 [30, 40, 35, 45, 0],
 [77, 80, 79, 85, 1],
 [50, 60, 65, 55, 0]
])


#1️⃣ Print only Math column
math_col = (data[:,0])
print(math_col)

#2️⃣ Print first 3 students (all subjects)
print (data[0:3,0:4])

#3️⃣ Print only students who passed
print(data[data[:, 4] == 1])


# 4️⃣ Print Math & Physics of students who failed
failed = data[data[:, 4] == 0]
print(failed[:, 0:2])



# 5️⃣ Print average marks of all passed students
passed = data[data[:, 4] == 1]
average = np.mean(passed[:, 0:4])
print(average)



# 6️⃣ Add 5 bonus marks to English subject of only passed students




# 7️⃣ Print students whose Math > 60 AND Physics > 70
