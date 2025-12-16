import json
import os

class ContactManager():
    def __init__(self, fileName = "Contact.json"):
        self.fileName = fileName
        self.People = []
        self.load_data()
        self.save_data()

    def load_data(self):
            if os.path.exists(self.fileName):
                with open(self.fileName, "r") as file:
                    self.People = json.load(file)
            else:
                 self.People = []

    def save_data(self):
         with open(self.fileName, "w") as file:
              json.dump(self.People, file, indent= 4)                           
                 

    def Add_Contact(self):
        Name = input("Enter your name: ")
        Gender = input("Enter your gender: ")
        Phone_Number = int(input("Enter your phone number: "))
        Email = input("Enter your Email: ")
        
        
        people = {
             "Name" : Name,
             "Gender" : Gender,
             "Phone Number" : Phone_Number,
             "Email" : Email
        }
        
        self.People.append(people)
        self.save_data()
        print("Student added successfully")

        
        
    
     
    
    