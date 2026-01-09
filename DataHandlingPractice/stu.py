students = []

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"

def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    
    m1 = float(input("Enter Math Marks: "))
    m2 = float(input("Enter Science Marks: "))
    m3 = float(input("Enter Computer Marks: "))

    total = m1 + m2 + m3
    percentage = total / 3
    grade = calculate_grade(percentage)

    student = {
        "name": name,
        "roll": roll,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)
    print("✅ Student Added Successfully\n")

def show_students():
    if not students:
        print("No data available\n")
        return

    print("\n------ All Student Results ------")
    for s in students:
        print(f"Name: {s['name']}")
        print(f"Roll: {s['roll']}")
        print(f"Total: {s['total']}")
        print(f"Percentage: {s['percentage']:.2f}%")
        print(f"Grade: {s['grade']}")
        print("-----------------------------")

def save_to_file():
    with open("students_result.txt", "w") as file:
        for s in students:
            file.write(f"{s['name']},{s['roll']},{s['total']},{s['percentage']},{s['grade']}\n")
    print("💾 Data saved to file\n")

while True:
    print("1. Add Student")
    print("2. Show All Results")
    print("3. Save to File")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        save_to_file()
    elif choice == "4":
        print("Thank you. Program Closed.")
        break
    else:
        print("Invalid choice\n")
