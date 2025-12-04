# List
Car = ["BMW", "Lemborgini", "Maruti", "Alto", "Kiwi"]

#Indexing
print(Car[0])
print(Car[-1])

#Slicing
print(Car[0:5])
print(Car[:])
print(Car[::2])

#Add Items
Car.append("BDA")
Car.insert(1,"Auto")



#Remove Items
Car.remove("Auto")
print(Car)
Car.pop(0)
print(Car)

#Some other useful methods
# fruits.sort()        # sort alphabetically
# fruits.reverse()     # reverse list
# print(len(fruits))   # number of elements

#Tuples
colors = ("red", "green", "blue")
print(colors[0:2])

#Sets
set1 = {1,2,3,4,5}
set1.add(6)
set1.remove(3)
set1.discard(5)
print(set1)

a = {1,2,3}
b = {3,4,5}

print(a | b)  # union {1,2,3,4,5}
print(a & b)  # intersection {3}
print(a - b)  # difference {1,2}



# DICTIONARIES

# Key-Value pairs

# Unordered (Python 3.7+ maintains insertion order)

# Mutable → can add/update/delete

# ✅ Example:
student = {
    "name": "Sunil",
    "age": 21,
    "city": "Nepal"
}

# Access Values
print(student["name"])  # Sunil
print(student.get("age"))  # 21

# Add/Update
student["email"] = "sunil@gmail.com"  # add
student["age"] = 22                   # update

# Remove
student.pop("city")
student.popitem()  # removes last inserted item

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)


