import json
import os


class ContactManager:
    def __init__(self, file_name="Contact.json"):
        self.file_name = file_name
        self.contacts = []
        self.load_data()

    def load_data(self):
        """Load contacts from JSON file."""
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                self.contacts = json.load(file)
        else:
            self.contacts = []

    def save_data(self):
        """Save contacts to JSON file."""
        with open(self.file_name, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        """Add a new contact."""
        name = input("Enter name: ")
        gender = input("Enter gender: ")
        phone = input("Enter phone number: ")
        email = input("Enter Email: ")

        contact = {
            "Name": name,
            "Gender": gender,
            "Phone Number": phone,
            "Email": email,
        }

        self.contacts.append(contact)
        self.save_data()
        print("Contact added successfully.")

    def view_contacts(self):
        """Display all contacts."""
        if not self.contacts:
            print("No contacts found.")
            return

        for index, contact in enumerate(self.contacts, start=1):
            print(f"\nContact {index}")
            for key, value in contact.items():
                print(f"{key}: {value}")

    def search_contacts(self, name):
        """Search contacts by partial or full name."""
        results = []
        for contact in self.contacts:
            if name.lower() in contact["Name"].lower():
                results.append(contact)
        return results

    def update_contact(self, name):
        """Update a contact by name."""
        results = self.search_contacts(name)

        if not results:
            print("No contact found.")
            return

        contact = results[0]

        print("\nCurrent Contact Details:")
        for key, value in contact.items():
            print(f"{key}: {value}")

        print("\nEnter new details (press Enter to keep old value):")
        new_name = input(f"Name [{contact['Name']}]: ")
        new_gender = input(f"Gender [{contact['Gender']}]: ")
        new_phone = input(f"Phone Number [{contact['Phone Number']}]: ")
        new_email = input(f"Email [{contact['Email']}]: ")

        if new_name:
            contact["Name"] = new_name
        if new_gender:
            contact["Gender"] = new_gender
        if new_phone:
            contact["Phone Number"] = new_phone
        if new_email:
            contact["Email"] = new_email

        self.save_data()
        print("Contact updated successfully.")

    def delete_contact(self, name):
        """Delete a contact by name."""
        results = self.search_contacts(name)

        if not results:
            print("No contact found.")
            return

        contact = results[0]
        self.contacts.remove(contact)
        self.save_data()
        print("Contact deleted successfully.")


def main():
    manager = ContactManager()

    def menu():
        print("\n----- Contact Management System -----")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_contact()
        elif choice == "2":
            manager.view_contacts()
        elif choice == "3":
            name = input("Enter name to search: ")
            results = manager.search_contacts(name)
            if results:
                print("\nContact(s) Found:")
                for contact in results:
                    for key, value in contact.items():
                        print(f"{key}: {value}")
                    print("-" * 20)
            else:
                print("Contact not found.")
        elif choice == "4":
            name = input("Enter name to update: ")
            manager.update_contact(name)
        elif choice == "5":
            name = input("Enter name to delete: ")
            manager.delete_contact(name)
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
