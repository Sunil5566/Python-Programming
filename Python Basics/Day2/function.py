#Function def:
def greeting():
    print("Hello World")

greeting()   

#Parameters and Arguments:

def Welcome(name):
    print("Welcome", name, end=".")
Welcome("Rashmi")  

#Printing whether the given number is odd or even 

def oddeven(x):
    if x % 2 == 0:
        print(f"{x} is Even number", end=".")
    else:
        print(f"{x} is Odd number", end=".")
oddeven(12)      
oddeven(11)      


#Returning function

def add(a,b):
    return a + b
result = add(2,3)
print(result)

#Default Parameter: If we give value it will print that otherwise it will look for default value

def greeting(name= "User"):
    print("Hello", name)

greeting()
greeting("Rashmi")    


#KeyWord Arguments
def student(name, age):
    print(name,age)

student(name = "Rashmi",age = 21)  


#*Args keyword:

def mul(*args):
    total = 1
    for arg in args:
        total *= arg
    return total
print(mul(2,3,4)) 

def display_name(*name):
    for name in name:
        print(name, end=" ")
display_name("Sunil", "Bhattarai")        


#kwargs Keyword:

def fruits_types_taste(**fruits):
    for key,value in fruits.items():
        print(f"{key}: {value} ")
fruits_types_taste(
    aamilo = "Grapes",
    sweety = "Apple",
    

)

def f1():
    s = 'I love GeeksforGeeks'
    def f2():
        print(s)
        
    f2()
f1()

#anonymous function: it is created using lambda keyword:
cube = lambda x: x*x*x
print(cube(3))
     
#doing square for the list

list1 = [2,5,7,8,2,4]
square = list(map(lambda x: x ** 2 ,list1))
print(square)     
