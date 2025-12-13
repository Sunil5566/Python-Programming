Students = []

def add_stu():
    Name = input("Enter your name: ")
    Age = int(input("Enter your age: "))
    Grade = float(input("Enter your grade: "))
    Address = input("Enter your address: ")
    Mbl_Num = int(input("Enter your mbl number: "))
    
    student = {
        "Name" : Name,
        "Age" : Age,
        "Grade" : Grade,
        "Address" : Address,
        "Mobile Number" : Mbl_Num
    }
    
    Students.append(student)

def view_stu():
    if not Students:
        print("No record found.")
        return

    for index,student in enumerate(Students, start = 1):
        print(f"\n Student {index}")

        for key, value in student.items():
            print(f"{key} : {value}")


def search_stu(name):
    for student in Students:
        if student["Name"].lower() == name.lower():
            return student
    return None  


def update_stu(name):
    student = search_stu(name)

    if student:
        student["Grade"] = float(input("Enter new grade: "))
        student["Address"] = input("Enter new address: ")
        print("Student updated successfully")

    else:
        print("No student found.")



