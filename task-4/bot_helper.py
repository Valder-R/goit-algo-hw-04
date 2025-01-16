def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        return "Contact with this name already exists"
    contacts[name] = phone
    save_contact(name, phone)
    return "Contact added."


def save_contact(name, phone):
    with open("task-4/contacts.txt","a",encoding="utf-8") as file:
        file.write(f"{name},{phone}\n")


def get_contacts():
    contacts = {}
    with open("task-4/contacts.txt", "r", encoding="utf-8") as file:
        lines = [el.strip() for el in file.readlines()]
        for line in lines:
            name, number = line.split(",")
            contacts[name] = number
    return contacts


def change_contact(args, contacts):
    name, phone = args
    if not name in contacts.keys():
        return "There is no contact with this name"
    contacts[name] = phone
    save_changes(name, contacts)
    return "Contact changed."


def save_changes(name, contacts):
    with open("task-4/contacts.txt","r+",encoding="utf-8") as file:
        content = file.read() 
        index = content.find(name)
        file.seek(index)
        file.write(f"{name},{contacts[name]}")


def show_phone(args, contacts):
    name = args[0]
    if not name in contacts.keys():
        return "There is no contact with this name"
    return f"Телефон: {contacts[name]}"


def show_all(contacts):
    listOfContacts = list()
    for key, value in contacts.items():
       listOfContacts.append(f"{key}, тел: {value}")
    return listOfContacts


def main():
    contacts = get_contacts()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            listOfContacts = show_all(contacts)
            for item in listOfContacts:
                print(item)
        elif command == "help":
            print("'close', 'exit' to stop the program")
            print("'add' to create new contact")
            print("'change' to change a contact")
            print("'phone' to see a phone number of person")
            print("'all' to print all contacts")
        else:
            print("Invalid command.")
            print("Try 'help' command")

if __name__ == "__main__":
    main()


