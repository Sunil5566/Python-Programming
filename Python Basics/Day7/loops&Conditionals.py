students = []

num_of_stud = int(input("Enter number of students you want to give info about: "))

for i in range(num_of_stud):
    name = input("Enter name of a student: ")
    marks = list(map(int, input("Enter marks in three subjects (comma separated): ").split(",")))

    student = {
        "Name": name,
        "Marks": marks
    }

    students.append(student)

def total_marks(marks):
    return sum(marks)

def average_marks(marks):
    return sum(marks) / len(marks)

for student in students:
    total = total_marks(student["Marks"])
    avg = average_marks(student["Marks"])

    if avg >= 90:
        grade = "A"
    elif 80 <= avg < 90:
        grade = "B"
    elif 70 <= avg < 80:
        grade = "C"
    else:
        grade = "D"

    print(f"\nStudent: {student['Name']}")
    print(f"Marks: {student['Marks']}")
    print(f"Total: {total}, Average: {avg:.2f}, Grade: {grade}")
