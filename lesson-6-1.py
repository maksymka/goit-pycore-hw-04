from typing import Tuple

def total_salary(path: str) -> Tuple[float, float]:
    """
    Аналізує файл із зарплатами та обчислює загальну та середню суму.
    """
    total: float = 0.0
    count: int = 0
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                try:
                    # Розділяємо рядок за комою
                    _, salary_str = line.split(",")
                    total += float(salary_str)
                    count += 1
                except ValueError:
                    print(f"Попередження: Некоректні дані у рядку: '{line}'")
                    continue

        if count == 0:
            return 0.0, 0.0
        
        average = total / count
        return total, average

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return 0.0, 0.0
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")
        return 0.0, 0.0

if __name__ == "__main__":
    # Тестові дані: створення файлу та виклик функції
    test_filename = "salary_file.txt"
    with open(test_filename, "w", encoding="utf-8") as f:
        f.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")

    total, average = total_salary(test_filename)
    if total > 0 or average > 0:
        print(f"Загальна сума: {total}, Середня зарплата: {average}")
