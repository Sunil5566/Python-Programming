class Student:
    def __init__ (self, name, rollno):
        self.name = name
        self.rollno = rollno

    def hello(self):
        print("Welcome student", self.name)

    def get_rollno(self):
        return self.rollno        
    
s1 = Student("Sunil", 27)
s1.hello()
print(s1.get_rollno())    