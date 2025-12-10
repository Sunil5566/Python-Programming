students = []

for i in range(3):
    print(f"Enter details of the students {i+1}")

    Name = input("Enter name of a student: ")
    Age = int(input("Enter age of a student: "))
    Subjects  = input("Enter 3 favourite subjects seperated by comma: ").split(",")
    Scores = tuple(map(int, input("Enter scores separated by comma: ").split(",")))

    Student = {
    "Name" : Name,
    "Age" : Age,
    "Subjects": Subjects,
    "Scores": Scores
    } 

    students.append(Student)

print("\n All studnets details: ")
for Student in students:
    print(Student)



