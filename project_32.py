class ContactManager:
    
    def __init__(self, logger):
        self.contacts = {}
        self.logger = logger
        

    def add_contact(self, name, number):
        self.contacts[name] = number
        self.logger.add_log(f"Added contact: {name} - Successfully")
        print(f"Contact added successfully")

    def view_contacts(self):
        if self.contacts:
            print("Available contacts:")
            for name, number in self.contacts.items():
                print(f"\nName: {name}")
                print(f"Number: {number}\n")
        else:
            print("No contact(s) available!")

    def search_contact(self, search):
        if search in self.contacts:
            self.logger.add_log(f"Searched contact: {search} - Found")
            print(f"Found ({search}): {self.contacts[search]}")
        else:
            self.logger.add_log(f"Searched contact: {search} - Not Found")
            print("Contact not found!")

    def delete_contact(self, delete):
        if delete in self.contacts:
            self.logger.add_log(f"Deleted contact: {delete} - Successfully")
            del self.contacts[delete]
        else:
            self.logger.add_log(f"Deleted contact: {delete} - Failed")
            print("Contact does not exist!!")


class Logger:
    def __init__(self):
        self.log = []

    def add_log(self, message):
        with open("log.txt", "a") as file:
            file.write(f"{message}\n")

    def view_logs(self):
        with open("log.txt", "r") as file:
            print(file.read())


logger = Logger()
manager = ContactManager(logger)

while True:

    print("\n----Welcome To Contact Manager v2.0----")
    
    print("""
    1. Add Contact
    2. View Contacts
    3. Search Contacts
    4. Delete Contact
    5. View Logs
    6. Exit
    """)

    try:

        command = int(input("Enter a command: "))
    
        commands = [1, 2, 3, 4, 5, 6]
        
    
        if command in commands and command == 1:
            
            name = input("\nEnter name: ").capitalize()
            number = input("Enter number: ")
            manager.add_contact(name, number)
            
        elif command in commands and command == 2:
            
            manager.view_contacts()
            
        elif command in commands and command == 3:
            
            search_input = input("Enter contact to search: ").capitalize()
            manager.search_contact(search_input)
            
        elif command in commands and command == 4:
            
            contact_to_delete = input("Enter contact to delete: ").capitalize()
            manager.delete_contact(contact_to_delete)
        elif command in commands and command == 5:
            print("\nLogs")
            logger.view_logs()
            
        elif command in commands and command == 6:
            print("Bye!!!")
            break
        else:
            print("Command not found!")
            
    except ValueError:
        print("Invalid command!")
    