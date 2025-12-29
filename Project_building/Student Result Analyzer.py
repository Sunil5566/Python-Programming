NumberOfStudent = int(input("Enter number of Students: "))

file = open("results.txt", "w")

for i in range(NumberOfStudent):
    name = input("Enter name of Student: ")
    marks_input = input("Enter marks of 5 subjects separated by comma: ")
    
    marks = list(map(int, marks_input.split(",")))
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "Fail"

    print(name, total, average, grade)

    file.write(f"{name} | Total: {total} | Avg: {average} | Grade: {grade}\n")

file.close()

print("\nAll results saved in results.txt")
