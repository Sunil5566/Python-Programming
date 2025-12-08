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

8. Handle Errors

Handle wrong inputs like strings instead of numbers for marks.

Handle file errors (like file not found) using try-except blocks.

9. Extra (Optional)

Calculate class average.

Find highest and lowest percentage.

Sort students by percentage.

Use modules like csv or os.

✅ What you’ll cover in Python with this project:

Variables and Data Types

Input/Output

Loops

Conditionals

Functions

OOP (Class & Object)

File Handling

Exception Handling

Lists/Dictionaries

Optional: Modules"""







Student_Name = input("Enter Student Name: ")
RollNum = int(input("Enter your RollNumber"))
Student_Class = input("Enter your class")
# Grade = float(input("Enter your grade"))

Student ={
    "Name" : Student_Name,
    "Roll Number": RollNum,
    "Class": Student_Class,
    # "Grade": Grade

}

Subjects = ["Maths", "Science", "Social", "Gk"]

marks = {}

for Subject in Subjects:
    while True:
        try:
         score = int(input(f"Enter marks for {Subject} (0-100)"))
         if 0 <= score <=100:
            marks[Subject] = score
            break
         else:
            print("Invalid input, Please enter a number between 0 and 100")

        except ValueError:
                       print("Invalid input, Please enter a number")

#to print marks
print("\n Marks Entered")
for Subject, score in marks.items():
     print(f"{Subject}: {score}")   



def calculate_total(marks):
     return sum(marks.values())

def calculate_percentage(total,max_marks):
     return (total/max_marks) * 100

total_marks = calculate_total(marks)
maxium_marks = len(marks) * 100
percentage = calculate_percentage(total_marks,maxium_marks)

print("Total Marks:", total_marks)
print("Percentage:", percentage)

print("Grade of students:")

# First, determine grade as a variable
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
student_data = f"Name: {Student_Name}, Roll: {RollNum}, Class: {Student_Class}, Marks: {marks}, Percentage: {percentage:.2f}, Grade: {grade}\n"

with open("student.txt","a") as f:
     f.write(student_data)


          

     


