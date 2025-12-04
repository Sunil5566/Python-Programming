import numpy as np

array_2d = np.array([[78,88,75,92],
                     [23,55,67,92],
                     [np.nan,30,44,56],
                     [90,89,76,80],
                     [100,np.nan,44,62],
                     [56,39,69,75],
                     [90,79,99,95],
                     [78,np.nan,99,96]])

NaN_Mean = np.nanmean(array_2d)
print("The nan mean of following driving center mean is: ",NaN_Mean)

col_Mean = np.nanmean(array_2d,axis=0)
print("Col mean is: ",col_Mean)

#Replace nan with col mean

#1.Find indices of nans
inds = np.where(np.isnan(array_2d))
array_2d[inds] = np.take(col_Mean,inds[1])
print("After nan replace with average value: \n",array_2d)

#Find totsl and averages of each student..

Total_Marks = np.sum(array_2d,axis=1)
print("Total marks of each student is: \n", Total_Marks)

Average_Marks_PerStd = np.mean(array_2d, axis=1)
print("Average marks of each student is: \n", Average_Marks_PerStd)

Average_Marks_PerSub = np.mean(array_2d, axis=0)
print("Average marks per Subject: \n", Average_Marks_PerSub)

highestAvgPersub = np.max(Average_Marks_PerSub)
print("Highest avg per subject: \n",highestAvgPersub)

lowestAvgPersub = np.min(Average_Marks_PerSub)
print("Lowest avg per subject: \n", lowestAvgPersub)

#to find the student with the highest total score
Topper_Index = np.argmax(Total_Marks)
print("Topper is Student", Topper_Index + 1, "with total marks:", Total_Marks[Topper_Index])

#addiing 5 bonus point in trffic rule section
array_2d[:,3] = array_2d[:,3] + 5
print("After bonus: \n",array_2d)

#Reshaping 2d array to 1d array
new_1dArray = array_2d.flatten()
print("After reshaping: \n",new_1dArray)









