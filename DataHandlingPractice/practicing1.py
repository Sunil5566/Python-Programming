numbers = [1, 2, 2, 3, 4, 1, 2, 3, 5, 4, 3]
count_dict = {}

for num in numbers:
    if num in count_dict:
        count_dict[num] = count_dict[num] + 1
    else:
        count_dict[num] = 1

print(count_dict)        


# marks = [56, 78, 45, 90, 67, 88, 39]
# TOtal = sum(marks)
# Average = sum / len(marks)
# print(Average)
# Highest = 
# Lowest = 