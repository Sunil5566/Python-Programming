students = []

# -------- INPUT --------
No_Of_Student = int(input("Enter number of students: "))

for i in range(No_Of_Student):
    name = input(f"\nEnter student {i+1} name: ")

    # Safe input for marks
    while True:
        try:
            marks_input = input("Enter marks in 3 subjects (comma separated): ")
            marks = [int(m) for m in marks_input.split(",")]

            if len(marks) != 3:
                print("❌ Please enter exactly 3 marks.")
                continue

            break
        except ValueError:
            print("❌ Invalid input! Use numbers only.")

    total = sum(marks)
    average = total / len(marks)

    # -------- GRADE --------
    if average >= 80:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    student = {
        "Name": name,
        "Marks": marks,
        "Total": total,
        "Average": average,
        "Grade": grade
    }

    students.append(student)

# -------- OUTPUT PER STUDENT --------
print("\n--- Student Report ---")
for s in students:
    print(f"{s['Name']} | Total: {s['Total']} | Avg: {s['Average']:.2f} | Grade: {s['Grade']}")

# -------- CLASS ANALYSIS --------
top_student = max(students, key=lambda s: s["Total"])
low_student = min(students, key=lambda s: s["Total"])

class_total = sum(s["Total"] for s in students)
class_average = class_total / No_Of_Student

pass_count = sum(1 for s in students if s["Average"] >= 40)

print("\n--- Class Analysis ---")
print(f"Top Scorer: {top_student['Name']} ({top_student['Total']})")
print(f"Lowest Scorer: {low_student['Name']} ({low_student['Total']})")
print(f"Class Average: {class_average:.2f}")
print(f"Passed Students: {pass_count}/{No_Of_Student}")
