from typing import List, Dict, Tuple


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """Розбирає введений рядок на команду та аргументи."""
    if not user_input.strip():
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Додає новий контакт або оновлює існуючий."""
    if len(args) < 2:
        return "Error: Give me name and phone please."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Змінює номер телефону для існуючого контакту."""
    if len(args) < 2:
        return "Error: Give me name and phone please."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return f"Error: Contact '{name}' not found."


def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """Виводить номер телефону за ім'ям."""
    if not args:
        return "Error: Enter user name."
    name = args[0]
    return contacts.get(name, f"Error: Contact '{name}' not found.")


def show_all(contacts: Dict[str, str]) -> str:
    """Виводить всі збережені контакти."""
    if not contacts:
        return "No contacts saved."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main() -> None:
    """Основний цикл управління ботом."""
    contacts: Dict[str, str] = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

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
