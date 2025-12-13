square = lambda x : x*x
print(square(5))

a = lambda x: x + 10
print(a(10))

#map() — Apply a function to every item
nums = [2,4,5,6]
square = list(map(lambda x: x*x , nums))
print(square)

#convert all string to int
data = ["2", "4", "6", "8"]

int_data = list(map(int,data))
print(int_data)

#filter() — Keep only elements that match a condition
nums1 = [1, 2, 3, 4, 5, 6]
evenNUm = list(filter(lambda x: x % 2 == 0,nums1))
print(evenNUm)

# keep names starting with "A"
names = ["Alex", "Bob", "Alice", "John"]
result = list(filter(lambda x: x.startswith("A"),names))
print(result)



