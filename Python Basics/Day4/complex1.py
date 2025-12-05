#Dendor Method

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
           

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

# num3 = num1.add(num2)  //with out using dendor method
#after using dendor method
num3 = num1 + num2
num3.showNumber()



#Create a class called order which stores items and its price.
#Use Dunder function __get__() to convey that:
# order1> order2 if price of order1 > price of order2

class order:
    def __init__(self, items, price):
        self.items = items
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price
         
                   

order1  = order("Chips", "20")                   
order2  = order("tea", "200")

print(order1 > order2)  #false