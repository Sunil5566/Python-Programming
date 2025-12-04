class Student:
    #Default constructor
    def __init__(self):
        pass

    #parameterize constructor
    def __init__(self, name,rollno):
        self.name = name
        self.rollno = rollno
        print("Data store in database")

s1 = Student("Sunil", 27)
print(s1.name, s1.rollno)

s2 = Student("Rashmi", 28)
print(s2.name, s2.rollno)