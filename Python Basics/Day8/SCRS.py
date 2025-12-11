# Student Card Report System
Student = []
Num_Of_Student = int(input("Enter number of students that you want to add: "))

for i in range(Num_Of_Student):
    Name = input("Enter Student name: ")
    try:
        Marks = [int(mark) for mark in input("Enter marks for students separated by comma: ").split(",")]

        if len(Marks) != 5:
            raise  ValueError("Please enter marks for 5 subjects.")
        
    except ValueError as e:
        print("Invalide error.",e)
        Marks = [0,0,0,0,0]    

    obtained_marks = sum(Marks)
    total_marks = len(Marks) * 100

    def Percentage(obtained_marks, total_marks):
        return (obtained_marks / total_marks) * 100
    
    percent = Percentage(obtained_marks, total_marks)

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

    Student.append({
        "Name" : Name,
        "Marks": Marks,
        "Obtained Marks" : obtained_marks,
        "Percentage" : percent,
        "Grade" : grade
    })

for s in Student:
    print("+" + "-"*40 + "+")
    print(f"| Student Name : {s['Name']:<25} |")
    print("+" + "-"*40 + "+")
    print(f"| Marks        : {', '.join(map(str, s['Marks'])):<25} |")
    print(f"| Total Marks  : {s['Obtained Marks']}/{len(s['Marks'])*100:<16} |")
    print(f"| Percentage   : {s['Percentage']:.2f}%{'':<16} |")
    print(f"| Grade        : {s['Grade']:<25} |")
    print("+" + "-"*40 + "+\n")

