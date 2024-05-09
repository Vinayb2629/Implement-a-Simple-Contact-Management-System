import json

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                contacts = json.load(file)
                return {name: Contact(**details) for name, details in contacts.items()}
        except FileNotFoundError:
            return {}

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump({contact.name: contact.__dict__ for contact in self.contacts.values()}, file)

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print("Contact already exists.")
        else:
            self.contacts[name] = Contact(name, phone, email)
            self.save_contacts()
            print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        for contact in self.contacts.values():
            print(contact)

    def edit_contact(self, name):
        if name in self.contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            self.contacts[name].phone = phone
            self.contacts[name].email = email
            self.save_contacts()
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

def main():
    manager = ContactManager()
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter the name of the contact: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            manager.add_contact(name, phone, email)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            name = input("Enter the name of the contact to edit: ")
            manager.edit_contact(name)
        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
