import json
import os
import time

# Путь к файлу для хранения заметок
FILE_PATH = "notes.json"
global id
id = 0
# Функция для загрузки заметок из файла
def load_notes():
    notes = []
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            notes = json.load(file)
    return notes

# Функция для сохранения заметок в файл
def save_notes(notes):
    with open(FILE_PATH, "w") as file:
        json.dump(notes, file, indent=4)

# Функция для добавления новой заметки
def add_note():
    notes = load_notes() 
    global id
    id +=1
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    date = time.strftime("%d/%m/%Y %H:%M:%S")
    note = {"id": id, "title": title, "body": body, "date": date}
    notes.append(note)
    save_notes(notes)
    print("Заметка добавлена успешно!")

# Функция для вывода списка заметок
def list_notes():
    notes = load_notes()
    if len(notes) > 0:
        print("Список заметок:")
        for note in notes:
            print("-" * 30)
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата создания/изменения: {note['date']}")
    else:
        print("Список заметок пуст!")

# Функция для редактирования заметки
def edit_note():
    notes = load_notes()
    id = int(input("Введите ID заметки для редактирования: "))
    found = False
    for note in notes:
        if note["id"] == id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            date = time.strftime("%d/%m/%Y %H:%M:%S")
            note["title"] = title
            note["body"] = body
            note["date"] = date
            found = True
            break
    if found:
        save_notes(notes)
        print("Заметка отредактирована успешно!")
    else:
        print("Заметка с таким ID не найдена!")

# Функция для удаления заметки
def delete_note():
    notes = load_notes()
    id = int(input("Введите ID заметки для удаления: "))
    note_index = -1
    for i in range(len(notes)):
        if notes[i]["id"] == id:
            note_index = i
            break
    if note_index != -1:
        del notes[note_index]
        save_notes(notes)
        print("Заметка удалена успешно!")
    else:
        print("Заметка с таким ID не найдена!")

# Основной цикл программы    
while True:
    print("\nМеню:")
    print("1. Добавить заметку")
    print("2. Вывести список заметок")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выход")
    choice = input("Введите номер операции: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        list_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        break
    else:
        print("Некорректный ввод. Повторите попытку.")