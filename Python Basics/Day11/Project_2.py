import os
import sys
import csv
from datetime import datetime


BASE_DIR = os.getcwd()
DATA_DIR = os.path.join(BASE_DIR, "data")
FILE_PATH = os.path.join(DATA_DIR, "students.csv")

if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)

if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Age", "Course", "Date"])

class Student:
    def __init__(self, sid, name, age, course):
        self.sid = sid
        self.name = name
        self.age = age
        self.course = course
        self.date = datetime.now().strftime("%d-%m-%Y %H:%M")

class StudentManager(Student):

    def add_student(self):
        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        student = Student(sid, name, age, course)

        with open(FILE_PATH, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([student.sid, student.name, student.age, student.course, student.date])

        print("✅ Student added successfully!")

    def view_students(self):
        with open(FILE_PATH, "r") as f:
            reader = csv.reader(f)
            data = list(reader)

            if len(data) <= 1:
                print("No students found.")
                return

            for row in data[1:]:
                print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]} | Date: {row[4]}")

    def search_student(self):
        search_id = input("Enter Student ID to search: ")

        with open(FILE_PATH, "r") as f:
            reader = csv.reader(f)
            found = False

            for row in reader:
                if row and row[0] == search_id:
                    print("Student Found:")
                    print(row)
                    found = True
                    break

            if not found:
                print("Student not found")

def main():
    manager = StudentManager("", "", "", "")

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            sys.exit(" Exiting program")
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
