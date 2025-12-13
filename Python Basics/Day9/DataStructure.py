#Tuples:
data1 = (1,2,3,4)
print(data1)

#Sets
 
data2 = {9,7,6,5,2,4,2,8,6,5}

data3 = {9,8,4,9,6,0,9,2,4,1}

print(data2 | data3) #union
print(data2 & data3) #intersection
print(data2 - data3)


#Nested list:

list1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(list1[2][2])
for row in list1:
    for value in row:
        print(value, end = " ")


"""Nested Dictionaries"""

students = {
    "101": {"name": "Alice", "age": 20},
    "102": {"name": "Bob", "age": 22}
}

for roll, info in students.items():
    print(roll, info["name"], info["age"])
