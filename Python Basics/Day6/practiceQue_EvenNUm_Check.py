#From a file containing numbers separated by comma , print the count of even numbers.
with open("Nmm.txt", "w") as f:
    f.write("10,33,56,76,89,56,122,43,753,74")

with open("Nmm.txt","r") as f:
    data = f.read()
    print(data)


numbers = data.split(",")

def count_even_num():
    count_even = 0
    for num in numbers:
       if int(num) % 2 ==0:
        count_even += 1
    print("Total even number: ", count_even)    

count_even_num()
       

