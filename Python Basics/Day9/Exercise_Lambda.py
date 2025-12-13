"""Exercise 1: Lambda (Warm-up)

Create a lambda function that:

Takes a number

Returns "Even" if the number is even, otherwise "Odd"

📌 Input: 7
📌 Output: "Odd"""

num = int(input("Enter a number: "))

chech_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

result = chech_even_odd(num)
print(result)







