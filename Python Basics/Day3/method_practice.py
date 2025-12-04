#Create student class that takes name and marks of 3 Subjects as arguments in constructor. 
# Then create a method to print the average

class Student:
    def __init__(self, name, sub1mark, sub2mark, sub3mark):
        self.name = name
        self.sub1mark = sub1mark
        self.sub2mark = sub2mark
        self.sub3mark = sub3mark


    def avr(self):
        average = ((self.sub1mark + self.sub2mark + self.sub3mark)/3  )   
        return average

s1 = Student("Sunil",80,90,90)
print(f"Average mark of {s1.name} is {s1.avr()}" )



#Using for loop
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avr(self):
        sum = 0
        for val in self.marks:
            sum += val
        average = sum / len(self.marks)
        print(f"Average marks of {self.name} is {average}")

s1 = Student("Sunil", [80, 90, 80])
s1.get_avr()                


