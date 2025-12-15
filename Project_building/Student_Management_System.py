import json
import os


class StudentManager:
    def __init__(self, filename="Student.json"):
        self.filename = filename
        self.Students = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.Students = json.load(file)
        else:
            self.Students = []

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.Students, file, indent=4)

    def add_stu(self, Name, Age, *marks, Grade="Not assigned", country="Nepal", **extra_info):

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
            "Marks": list(marks)  
        }

        student.update(extra_info)

        self.Students.append(student)
        self.save_data()
        print("Student added successfully")

    def view_stu(self):
        if not self.Students:
            print("No record found.")
            return

        for index, student in enumerate(self.Students, start=1):
            print(f"\nStudent {index}")
            for key, value in student.items():
                print(f"{key} : {value}")

    def search_stu(self, name):
        for student in self.Students:
            if student["Name"].lower() == name.lower():
                return student, True
        return None, False

    def update_stu(self, name, *marks, **updates):
        student, found = self.search_stu(name)

        if not found:
            print("No student found.")
            return

        if marks:
            student["Marks"] = list(marks)

        for key, value in updates.items():
            if key in student:
                student[key] = value

        self.save_data()
        print("Student updated successfully")

    def delete_stu(self, name):
        student, found = self.search_stu(name)

        if found:
            self.Students.remove(student)
            self.save_data()
            print("Deleted student data successfully.")
        else:
            print("No student data found.")


def main():
    manager = StudentManager()

    def menu():
        print("\n----- Student Management System -----")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))

            marks_input = input("Enter marks (space separated): ")
            marks = tuple(map(int, marks_input.split())) if marks_input else ()

            manager.add_stu(name, age, *marks)

        elif choice == "2":
            manager.view_stu()

        elif choice == "3":
            name = input("Enter student name to update: ")
            new_address = input("Enter new address: ")
            manager.update_stu(name, Address=new_address)

        elif choice == "4":
            name = input("Enter student name to delete: ")
            manager.delete_stu(name)

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice")


main()
