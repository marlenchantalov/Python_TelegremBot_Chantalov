import os

def file_exists(note_name):
    filename = f"{note_name}.txt"
    if not os.path.isfile(filename):
        print(f"Заметка с названием {note_name} не найдена.")
        return None
    return filename

def create_note():
    note_name = input("Введите название заметки: ")
    note_text = input("Введите текст заметки: ")
    with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
        file.write(note_text)
    print(f"Новая заметка {note_name} создана.")

def read_note():
    note_name = input("Введите название заметки: ")
    filename = file_exists(note_name)
    if filename:
        with open(filename, "r", encoding="utf-8") as file:
            print("Содержимое заметки:")
            print(file.read())

def edit_note():
    note_name = input("Введите название заметки для редактирования: ")
    filename = file_exists(note_name)
    if filename:
        with open(filename, "r", encoding="utf-8") as file:
            print("Текущее содержимое заметки:")
            print(file.read())
        new_content = input("Введите новый текст заметки: ")
        with open(filename, "w", encoding="utf-8") as file:
            file.write(new_content)
        print(f"Заметка {note_name} была обновлена.")

def delete_note():
    note_name = input("Введите название заметки для удаления: ")
    filename = file_exists(note_name)
    if filename:
        os.remove(filename)
        print(f"Заметка {note_name} была удалена.")

def main():
    actions = {"1": create_note, "2": read_note, "3": edit_note, "4": delete_note}
    while True:
        print("\nМеню управления заметками:\n1. Создать заметку\n2. Прочитать заметку\n3. Редактировать заметку\n4. Удалить заметку\n5. Выйти")
        choice = input("Выберите действие (1-5): ")
        if choice in actions:
            actions[choice]()
        elif choice == "5":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 5.")

if __name__ == "__main__":
    main()
