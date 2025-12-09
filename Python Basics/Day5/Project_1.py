"""Project Idea: Student Marks and Percentage Calculator

Scenario:
You are building a program for a school to manage students’ marks, calculate their percentage, grade them, and save the data for later use.

Step-by-Step Guide
1. Ask for Student Details

Input: Name, Roll Number, Class/Grade.

Store this data in variables or a dictionary.

2. Input Marks

Ask the user to input marks for multiple subjects (like Math, Science, English, etc.).

Validate input: marks should be between 0 and 100.

Use a loop to get marks for all subjects.

3. Calculate Total and Percentage

Total marks = sum of all subjects.

Percentage = (Total marks / Maximum marks) × 100.

Use functions to calculate total and percentage.

4. Assign Grades

Based on percentage, assign a grade:

≥ 90% → A+

80–89% → A

70–79% → B+

60–69% → B

50–59% → C

<50% → Fail

Use if-elif-else statements.

5. Store Data in a File

Save student info, marks, percentage, and grade in a text file or CSV file.

Each student’s data should be on a new line.

Use file handling concepts (open, write, read).

6. Optional: Use OOP

Create a Student class with:

Attributes: name, roll number, marks, percentage, grade.

Methods: calculate_percentage(), assign_grade(), show_report().

Store multiple students in a list.

`7. Add Features

Ask the user whether they want to:

Add a new student

Show all students

Search a student by name or roll number

Exit program

Use while loop and menu-driven system.`



9. Extra (Optional)

Calculate class average.

Find highest and lowest percentage.

Sort students by percentage.

Use modules like csv or os.

"""








import csv

SUBJECTS = ["Maths", "Science", "Social", "Gk"]

# ---------------- FUNCTIONS --------------------

def calculate_total(marks):
    return sum(marks.values())

def calculate_percentage(total, max_marks):
    return (total / max_marks) * 100

def add_student():
    name = input("Enter Student Name: ")
    roll = int(input("Enter Roll Number: "))
    student_class = input("Enter Class: ")

    marks = {}
    for subject in SUBJECTS:
        while True:
            try:
                score = int(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= score <= 100:
                    marks[subject] = score
                    break
                else:
                    print("Invalid input! Enter marks between 0 and 100.")
            except ValueError:
                print("Invalid input! Enter a number.")

    total = calculate_total(marks)
    max_marks = len(SUBJECTS) * 100
    percentage = calculate_percentage(total, max_marks)

    # Assign grade
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B+"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    student_row = [name, roll, student_class] + [marks[s] for s in SUBJECTS] + [total, round(percentage,2), grade]

    # Write to CSV
    try:
        try:
            with open("students.csv", "r") as f:
                pass
        except FileNotFoundError:
            with open("students.csv", "w", newline="") as f:
                writer = csv.writer(f)
                header = ["Name", "Roll", "Class"] + SUBJECTS + ["Total", "Percentage", "Grade"]
                writer.writerow(header)

        with open("students.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(student_row)

        print("\nStudent added successfully!")
    except Exception as e:
        print("Error saving student:", e)

def show_all_students():
    try:
        with open("students.csv", "r") as f:
            reader = csv.reader(f)
            data = list(reader)
            if len(data) <= 1:
                print("No student records found.")
            else:
                print("\n--- All Students ---")
                for row in data:
                    print(row)
    except FileNotFoundError:
        print("No student file found!")

def search_student():
    key = input("Enter student name or roll number to search: ")
    found = False
    try:
        with open("students.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0].lower() == "name":  # skip header
                    continue
                if key.lower() in row[0].lower() or key == row[1]:
                    print(row)
                    found = True
        if not found:
            print("No student found with that detail.")
    except FileNotFoundError:
        print("No student file found!")

# ---------------- EXTRA FEATURES --------------------

def class_average():
    try:
        with open("students.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            percentages = [float(row[-2]) for row in reader]
            if len(percentages) == 0:
                print("No student data to calculate average.")
                return
            avg = sum(percentages) / len(percentages)
            print(f"Class Average Percentage: {avg:.2f}%")
    except FileNotFoundError:
        print("No student file found!")

def highest_lowest():
    try:
        with open("students.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)
            data = list(reader)
            if not data:
                print("No student data available.")
                return
            data_sorted = sorted(data, key=lambda x: float(x[-2]), reverse=True)
            print("Highest Percentage:")
            print(data_sorted[0])
            print("Lowest Percentage:")
            print(data_sorted[-1])
    except FileNotFoundError:
        print("No student file found!")

def sort_by_percentage():
    try:
        with open("students.csv", "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            data = list(reader)
            if not data:
                print("No student data available.")
                return
            data_sorted = sorted(data, key=lambda x: float(x[-2]), reverse=True)
            print("\n--- Students Sorted by Percentage (High to Low) ---")
            print(header)
            for row in data_sorted:
                print(row)
    except FileNotFoundError:
        print("No student file found!")

# ---------------- MENU SYSTEM --------------------

while True:
    print("\n----- Menu Driven -----")
    print("1: Add a new student")
    print("2: Show all students")
    print("3: Search a student")
    print("4: Class Average")
    print("5: Highest & Lowest Percentage")
    print("6: Sort Students by Percentage")
    print("7: Exit program")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_all_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        class_average()
    elif choice == "5":
        highest_lowest()
    elif choice == "6":
        sort_by_percentage()
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
