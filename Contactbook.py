class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        for i, contact in enumerate(self.contacts):
            print(f"{i+1}. {contact.name} - {contact.phone}")

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query.lower() in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, index, contact):
        if 0 < index <= len(self.contacts):
            self.contacts[index-1] = contact

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            del self.contacts[index-1]

def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            manager.add_contact(contact)
        elif choice == 2:
            manager.view_contact_list()
        elif choice == 3:
            query = input("Enter name or phone number to search: ")
            results = manager.search_contact(query)
            for result in results:
                print(f"{result.name} - {result.phone}")
        elif choice == 4:
            index = int(input("Enter the index of the contact to update: "))
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact = Contact(name, phone, email, address)
            manager.update_contact(index, contact)
        elif choice == 5:
            index = int(input("Enter the index of the contact to delete: "))
            manager.delete_contact(index)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
