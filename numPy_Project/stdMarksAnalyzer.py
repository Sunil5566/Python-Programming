import numpy as np

marks_Of_Each_Std = np.array([[50,78,98,67],
                              [98,56,78,33],
                              [23,56,66,76]])

total_marks_of_each_std = marks_Of_Each_Std.sum(axis=1)
print("Total marks of student : " + str(total_marks_of_each_std))

averageMarkOfStd = marks_Of_Each_Std.mean(axis=1)
print("Average marks of std : " + str(averageMarkOfStd))

HighestMark_std = marks_Of_Each_Std.max(axis=1) 
print("Highest marks of each std: " + str(HighestMark_std))

LowestMark_std = marks_Of_Each_Std.min(axis = 1)
print("Lowest marks of each std: " + str(LowestMark_std))

HighestScoringStd = marks_Of_Each_Std.argmax(axis=0)
print("Highest scoring student: " + str(HighestScoringStd))

MarksGreaterThan50 = marks_Of_Each_Std[marks_Of_Each_Std >= 50]
print("Makrs more than 49 " ,MarksGreaterThan50)
TotalPeopleHavingMarksGreaterThan50 = MarksGreaterThan50.size
print("total std: ", TotalPeopleHavingMarksGreaterThan50)








