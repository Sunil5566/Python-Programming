"""
Create a class Book with attributes: title, author, and price.
Add a method bookInfo() that prints all details.
Create 2 objects and display their information.

👉 This checks: class, object, constructor, methods
"""

class Book:
    def __init__(self, title, author,price):
        self.title = title
        self.author = author
        self.price = price 

    def bookInfo(self):
           print(f"Title = {self.title}, Author = {self.author}, Price ={self.price}")       

b1 = Book("Hello","Rashmi","1500")        
b2 = Book("Hi","Sunil","1200")      
b1.bookInfo()
b2.bookInfo()  
                


"""
OOP Practice Question 2 — Inheritance

Create a class Vehicle with attributes:

brand

speed

And a method:

showInfo() → prints brand & speed

Then create a subclass Car that:

Inherits from Vehicle

Has one extra attribute: seats

Overrides showInfo() to also print seats

Finally:

Create one object of Car and display all details.
"""
class Vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def showInfo(self):
         print(f"Brand ={self.brand}, speed = {self.speed}")

class Car(Vehicle):
    def __init__(self,brand,speed,seat):
        super().__init__(brand,speed)
        self.seat = seat

    def showInfo(self):   # method overriding
        print(f"Brand = {self.brand}, Speed = {self.speed}, Seats = {self.seat}")    


car1 = Car("Toyato", "200km/h", "12")
car1.showInfo()







"""Create a base class Animal with a method:

sound()


Then create two subclasses:

Dog → prints "Bark!"

Cat → prints "Meow!"

Create objects of both classes and call sound().

👉 Goal:
Demonstrate polymorphism where the same method name behaves differently in different classes."""

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Bark!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

Dog1 = Dog()
Cat1 = Cat()

Dog1.sound()
Cat1.sound()   





"""OOP Practice Question 4 — Operator Overloading

Create a class ComplexNumber with attributes:

real

img

Add:

1. __add__ operator overloading

So that you can do:

c3 = c1 + c2


and it should return a new ComplexNumber object.

2. A method show()

that prints the number in this format:

a + bi

Finally:

Create two objects

Add them using +

Print the result using .show()"""

class ComplexNumber():
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")    

    def  __add__(c1,c2):
        newReal = c1.real + c2.real
        newImg = c1.img + c2.img
        return ComplexNumber(newReal , newImg)

c1 = ComplexNumber(2,4)
c2 = ComplexNumber(5,1)
c3 = c1 + c2
c3.showNumber()        


"""OOP Practice Question 5 — Encapsulation + Getter/Setter (@property)

Create a class BankAccount with:

private attribute: __balance

method deposit(amount)

method withdraw(amount)

use @property to get balance

use @balance.setter to update balance BUT

new balance cannot be negative

if negative, show: "Invalid balance"

Finally:

Create an object

Do deposit, withdraw

Print final balance"""




