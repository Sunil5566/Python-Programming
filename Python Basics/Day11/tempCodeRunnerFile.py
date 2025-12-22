"""Functional Requirements
1️⃣ Student Input

Ask user how many students

For each student:

Name

Marks in 3 subjects

Store data properly (not random variables)

2️⃣ Processing (LOGIC PART)

For each student:

Calculate total marks

Calculate average

Assign grade:

A → avg ≥ 80

B → avg ≥ 60

C → avg ≥ 40

F → avg < 40

3️⃣ Class Analysis

Find top scorer

Find lowest scorer

Calculate class average

Count how many students passed (avg ≥ 40)"""


students = []
No_Of_Student = int(input("Enter number of students: "))

for i in range(No_Of_Student):
    Name = input(f"Enter student name for Student{i+1} name: ")
    MarksIn3Sub = input("Marks in threee subjects seperated by commma: ")
    
    mark_list = [int(m) for m in MarksIn3Sub.split(",")]



    student = {
        "Name" : Name,
        "Marks" : mark_list
    }
    
    students.append(student)


for student in students:
    total_marks = sum(student["Marks"])
    average = total_marks / len(student["Marks"])
    print(f"{student['Name']} - Total: {total_marks}, Averge: {average}")

