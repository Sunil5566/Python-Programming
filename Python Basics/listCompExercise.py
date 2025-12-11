#Create a list of numbers from 1 to 20
list1 = [x for x in range(1,20)]
print(list1)

#Create a list of squares of numbers from 1 to 10
list2 = [x*x  for x in range (1,10)]
print(list2)

#Create a list of even numbers between 1 and 30
list3 = [x for x in range (1,30)if x % 2 ==0 ]
print(list3)

#From a list of words, create a list of words that start with 'A'
words = ["Apple", "Banana", "Avocado", "Kiwi", "Apricot"]
list4 = [x for x in words if "a" and "A" in x]
print(list4)

"""Conditional mapping

For a list of integers, replace multiples of 3 with "Fizz" and multiples of 5 with "Buzz". If both, "FizzBuzz".

numbers = [1,3,5,15,16]
Expected output: [1, 'Fizz', 'Buzz', 'FizzBuzz', 16]"""

List_Of_Int = [1, 3, 5, 15, 16, 24, 65, 78, 98, 60]

list5 = [
    "FizzBuzz" if x % 3 == 0 and x % 5 == 0 
    else "Fizz" if x % 3 == 0 
    else "Buzz" if x % 5 == 0 
    else x
    for x in List_Of_Int
]

print(list5)

"""Flatten a 2D list
matrix = [[1,2,3], [4,5,6], [7,8,9]]
Expected output: [1,2,3,4,5,6,7,8,9]"""

matrix = [[1,2,3], [4,5,6], [7,8,9]]
List6 = [x for row in matrix for x in row]
print(List6)


"""From a list of words, get the length of each word
words = ["Python", "is", "awesome"]
Expected output: [6, 2, 7]"""
words = ["Python", "is", "awesome"]
List7 = [len(word) for word in words ]
print(List7)





