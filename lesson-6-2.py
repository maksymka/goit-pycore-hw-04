def get_cats_info(path):
    """
    Читає файл із даними про котів і перетворює їх на список словників.
    
    Параметри:
    path (str): Шлях до текстового файлу.
    
    Повертає:
    list: Список словників з ключами 'id', 'name', 'age'.
    """
    cats_list = []
    
    try:
        # Відкриваємо файл за допомогою менеджера контексту 'with'
        # Встановлюємо encoding="utf-8" для підтримки різних символів
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                # Видаляємо зайві символи перенесення рядка та пробіли по краях
                cleaned_line = line.strip()
                
                # Пропускаємо порожні рядки
                if not cleaned_line:
                    continue
                
                # Розділяємо рядок за комою
                # Очікуємо 3 елементи: id, name, age
                try:
                    cat_id, name, age = cleaned_line.split(",")
                    
                    # Створюємо словник для поточного кота
                    cat_dict = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    
                    # Додаємо словник до загального списку
                    cats_list.append(cat_dict)
                    
                except ValueError:
                    print(f"Попередження: Рядок '{cleaned_line}' має некоректний формат.")
                    continue
                    
        return cats_list

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")
        return []

# Приклад тестування:
# Створимо файл для тесту (якщо його ще немає)
# with open("cats_file.txt", "w", encoding="utf-8") as f:
#     f.write("60b90c1c13067a15887e1ae1,Tayson,3\n"+
#             "60b90c2413067a15887e1ae2,Vika,1\n"+
#             "60b90c2e13067a15887e1ae3,Barsik,2\n"+
#             "60b90c3b13067a15887e1ae4,Simon,12\n"+
#             "60b90c4613067a15887e1ae5,Tessi,5")


cats_info = get_cats_info("cats_file.txt")

#Виводимо результат построково, щоб гарно виглядало:
for cat in cats_info:
    print(f"ID: {cat['id']}, Ім'я: {cat['name']}, Вік: {cat['age']}")