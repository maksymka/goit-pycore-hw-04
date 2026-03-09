from typing import List, Dict


def get_cats_info(path: str) -> List[Dict[str, str]]:
    """
    Читає файл із даними про котів і перетворює їх на список словників.
    """
    cats_list: List[Dict[str, str]] = []
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue
                
                try:
                    cat_id, name, age = cleaned_line.split(",")
                    cats_list.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
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


if __name__ == "__main__":
    test_filename = "cats_file.txt"
    with open(test_filename, "w", encoding="utf-8") as f:
        f.write("60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1")

    cats_info = get_cats_info(test_filename)
    for cat in cats_info:
        print(f"ID: {cat['id']}, Ім'я: {cat['name']}, Вік: {cat['age']}")
