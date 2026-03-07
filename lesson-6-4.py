def parse_input(user_input):
    """Розбирає введений рядок на команду та аргументи."""
    if not user_input.strip():
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """Додає новий контакт або оновлює існуючий."""
    if len(args) < 2:
        return "Error: Give me name and phone please."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """Змінює номер телефону для існуючого контакту."""
    if len(args) < 2:
        return "Error: Give me name and phone please."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Error: Contact '{name}' not found."

def show_phone(args, contacts):
    """Виводить номер телефону за ім'ям."""
    if not args:
        return "Error: Enter user name."
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Error: Contact '{name}' not found."

def show_all(contacts):
    """Виводить всі збережені контакти."""
    if not contacts:
        return "No contacts saved."
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    """Основний цикл управління ботом."""
    contacts = {}
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
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()