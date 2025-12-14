Students = []

def add_stu(Name, Age, *marks, Grade="Not assigned", country="Nepal", **extra_info):

    user_grade = input("Enter your grade (or press Enter to skip): ")
    if user_grade:
        Grade = float(user_grade)
    
    Address = input("Enter address: ")
    Mbl_Num = input("Enter mobile number: ")
    
    student = {
        "Name": Name,
        "Age": Age,
        "Grade": Grade,
        "Address": Address,
        "Mobile Number": Mbl_Num,
        "Country": country,
        "Marks": marks  
    }
    
    student.update(extra_info)
    
    Students.append(student)
    print("Student added successfully")

def view_stu():
    if not Students:
        print("No record found.")
        return

    for index, student in enumerate(Students, start=1):
        print(f"\nStudent {index}")
        for key, value in student.items():
            print(f"{key} : {value}")

def search_stu(name):
    for student in Students:
        if student["Name"].lower() == name.lower():
            return student
    return None

def update_stu(name, **updates):
    student = search_stu(name)

    if not student:
        print("No student found.")
        return

    for key, value in updates.items():
        if key in student:
            student[key] = value

    print("Student updated successfully")

def delete_stu(name):
    student = search_stu(name)

    if student:
        Students.remove(student)
        print("Deleted student data successfully.")
    else:
        print("No student data found.")
