import json

# -------------------- LOAD PREVIOUS DATA --------------------
try:
    with open("students.json", "r") as f:
        Student = json.load(f)
        print("Loaded previous student records.\n")
except FileNotFoundError:
    Student = []
    print("No previous data found. Starting fresh.\n")


# -------------------- INPUT SECTION --------------------
Num_Of_Student = int(input("Enter number of students that you want to add: "))

for i in range(Num_Of_Student):
    print(f"\n--- Enter details for Student {i + 1} ---")
    Name = input("Enter Student name: ")

    try:
        Marks = [int(mark) for mark in input("Enter marks for 5 subjects separated by comma: ").split(",")]

        if len(Marks) != 5:
            raise ValueError("You must enter exactly 5 marks!")
    
    except ValueError as e:
        print("Invalid input! Error:", e)
        print("Defaulting marks to 0 for all 5 subjects.")
        Marks = [0, 0, 0, 0, 0]


    # --- Calculations ---
    obtained_marks = sum(Marks)
    total_marks = len(Marks) * 100
    percent = (obtained_marks / total_marks) * 100

    # --- Grade calculation ---
    if percent >= 90:
        grade = "A"
    elif 80 <= percent < 90:
        grade = "B"
    elif 70 <= percent < 80:
        grade = "C"
    elif 60 <= percent < 70:
        grade = "D"
    else:
        grade = "F"

    # --- Append to data list ---
    Student.append({
        "Name": Name,
        "Marks": Marks,
        "Obtained Marks": obtained_marks,
        "Percentage": percent,
        "Grade": grade
    })


# -------------------- SAVE DATA TO JSON --------------------
with open("students.json", "w") as f:
    json.dump(Student, f, indent=4)

print("\nAll student data saved successfully!\n")


# -------------------- PRINT CLEAN REPORT --------------------
for s in Student:
    print("+" + "-"*40 + "+")
    print(f"| Student Name : {s['Name']:<25} |")
    print("+" + "-"*40 + "+")
    print(f"| Marks        : {', '.join(map(str, s['Marks'])):<25} |")
    print(f"| Total Marks  : {s['Obtained Marks']}/{len(s['Marks']) * 100:<16} |")
    print(f"| Percentage   : {s['Percentage']:.2f}%{'':<16} |")
    print(f"| Grade        : {s['Grade']:<25} |")
    print("+" + "-"*40 + "+\n")
