#Default argument

def greet(name="EveryOne"):
    print(f"Hello {name}")

greet("")
greet("Sunil")


#Keyword Argument

def Car(name, model):
    print(f"My car name is {name} and model is {model}")

Car("BMW", "2022")
Car("Lemborgini", "2024")    



#*args
def multiply(*args):
    result = 1
    for nums in args:
        result *= nums
    return result 

print(multiply(2,3,4))   
    


