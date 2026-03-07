def total_salary(path):
    """
    Аналізує файл із зарплатами та обчислює загальну та середню суму.
    
    Параметри:
    path (str): Шлях до текстового файлу.
    
    Повертає:
    tuple: (загальна_сума, середня_зарплата) або (0, 0) у разі помилки.
    """
    total = 0
    count = 0
    
    try:
        # Використовуємо менеджер контексту 'with' для безпечного відкриття файлу
        # Вказуємо кодування utf-8 для коректного читання прізвищ
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                # Видаляємо зайві пробіли та символи переходу на новий рядок
                line = line.strip()
                if not line:  # Пропускаємо порожні рядки, якщо вони є
                    continue
                
                try:
                    # Розділяємо рядок за комою
                    name, salary_str = line.split(",")
                    # Перетворюємо зарплату на число (float для точності або int)
                    total += float(salary_str)
                    count += 1
                except ValueError:
                    print(f"Попередження: Некоректні дані у рядку: '{line}'")
                    continue

        # Обчислюємо середню зарплату
        if count == 0:
            return 0, 0
        
        average = total / count
        return total, average

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")
        return 0, 0

# Приклад використання:
# Створимо файл для тесту (якщо його ще немає):
# with open("salary_file.txt", "w", encoding="utf-8") as f:
# f.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")

total, average = total_salary("salary_file.txt")
if total > 0 or average > 0:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")