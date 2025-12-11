
#Here we get a fruits that has a in their :

#..............Method-1..................
# fruits = ["Mango", "Orange", "Grapes", "Kiwi", "Apple", "Banana"]
# new_list=[]

# for x in fruits:
#     if "a" in x:
#         new_list.append(x)

# print(new_list)

#............Method-2.......................
fruits = ["Mango", "Orange", "Grapes", "Kiwi", "Apple", "Banana"]
newList = [x for x in fruits if "a" in x]
print(newList)



#...............................Create a list of squre...............
square = [x*x for x in range(1,6)]
print(square)

cube = [x**3 for x in range(1,6)]
print(cube)

#Filter even numbers (using condition)
even_num = [x for x in range(1,10) if x % 2 == 0]
print(even_num)


#Convert list of strings to uppercase
list = ["Mango", "Orange", "Grapes", "Kiwi", "Apple", "Banana"]
UpperCaseList = [fruit.upper() for fruit in list]
print(UpperCaseList)

#Convert list of strings to lowercase
list1 = ["Mango", "Orange", "Grapes", "Kiwi", "Apple", "Banana"]
LowerCaseList = [li.lower() for li in list1]
print(LowerCaseList)

#Use IF–ELSE inside comprehension
numbers = [2,5,76,89,55,66,46,3321,76,78,90,77,44]
result = ["Even" if x % 2 ==0 else "Odd" for x in numbers]
print(result)



