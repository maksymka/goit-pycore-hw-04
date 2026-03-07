import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama для підтримки Windows
init(autoreset=True)

def visualize_directory_structure(path, indent=""):
    """
    Рекурсивно виводить структуру директорії з кольоровим маркуванням.
    """
    try:
        base_path = Path(path)
        
        # Отримуємо відсортований список вмісту (спочатку папки, потім файли)
        items = sorted(base_path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        
        for index, item in enumerate(items):
            # Визначаємо, чи це останній елемент у поточному списку для малювання символів
            is_last = (index == len(items) - 1)
            connector = "┗ " if is_last else "┣ "
            
            if item.is_dir():
                # Виводимо папку синім кольором
                print(f"{indent}{connector}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
                
                # Рекурсивний виклик для піддиректорії
                new_indent = indent + ("  " if is_last else "┃ ")
                visualize_directory_structure(item, new_indent)
            else:
                # Виводимо файл зеленим кольором
                print(f"{indent}{connector}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
                
    except PermissionError:
        print(f"{indent}{Fore.RED}[Доступ заборонено]{Style.RESET_ALL}")

def main():
    # Перевірка наявності аргументу командного рядка
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Використання: python hw03.py <шлях_до_директорії>{Style.RESET_ALL}")
        return

    target_path = Path(sys.argv[1])

    # Валідація шляху
    if not target_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{target_path}' не існує.{Style.RESET_ALL}")
        return
    if not target_path.is_dir():
        print(f"{Fore.RED}Помилка: '{target_path}' не є директорією.{Style.RESET_ALL}")
        return

    # Вивід кореневої папки
    print(f"{Fore.CYAN}📦 {target_path.name}{Style.RESET_ALL}")
    visualize_directory_structure(target_path)

if __name__ == "__main__":
    main()