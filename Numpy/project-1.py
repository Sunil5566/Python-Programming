import numpy as np

students = np.array([
    [78, 85, 90, 88, 92],   # Student 1
    [60, 65, 70, 72, 68],   # Student 2
    [90, 95, 98, 92, 96],   # Student 3
    [55, 58, 60, 62, 57],   # Student 4
    [88, 82, 85, 80, 86]    # Student 5
])

print("Marks Matrix:\n", students)



## Step-2: Total Marks of Each Student

total = np.sum(students, axis=1)
print("Total Marks:", total)


##  Step-3: Percentage of Each Student

percentage = (total / 500) * 100
print("Percentage:", percentage)


##  Step-4: Find Topper

topper_index = np.argmax(percentage)
print("Topper Student Number:", topper_index + 1)
print("Topper Percentage:", percentage[topper_index])


##  Step-5: Subject-wise Average

subject_avg = np.mean(students, axis=0)
print("Subject Wise Average:", subject_avg)



grades = []

for p in percentage:
    if p >= 90:
        grades.append("A+")
    elif p >= 80:
        grades.append("A")
    elif p >= 70:
        grades.append("B")
    elif p >= 60:
        grades.append("C")
    else:
        grades.append("Fail")

print("Grades:", grades)
