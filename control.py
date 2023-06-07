# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой
#  [id, title, body, date]

from datetime import *
import json

def load():

    fname = 'notes.json'
    with open(fname, 'r', encoding='utf-8') as em:
        notes = json.load(em)
    print('Заметки успешно загружены')
    return notes

def save():
    with open('notes.json', 'w', encoding='utf-8') as em:
        em.write(json.dumps(notes, ensure_ascii=False))

def printNote(i):
    print(f'Номер заметки: {notes[i][0]}')
    print(f'Заголовок: {notes[i][1]}')
    print(f'Заметка: {notes[i][2]}')
    print(f'Дата: {notes[i][3]}')
    print()

print('Программа работы с заметками')
try:
    notes = load()
except:
    notes = []
    print('Заметки не найдены. Создана новая история')
while True:
    command = input('Введите команду :').lower()
    match command:
        case 'add':
            print('Добавление заметки')
            title = input('Введите заголовок: ')
            body = input('Введите заметку: ')
            note_date = datetime.now()
            id = notes[-1][0] + 1
            notes.append([id, title, body, str(note_date.strftime("%d-%m-%Y"))])
            print('Заметка добавлена')
            save()
        case 'list':
            for i in notes:
                printNote(notes.index(i))
        case 'search':
            search_date = input('Введите  дату в формате ДД-ММ-ГГГГ:')
            try:
                search_date = str(datetime.strptime(search_date, "%d-%m-%Y").strftime("%d-%m-%Y"))
                isFound = False
                print()
                for i in notes:
                    if i[3] == search_date:                      
                        printNote(notes.index(i))
                        isFound = True
                if isFound == False:
                    print('Записей за эту дату не найдено')
            except:
                print('Некорректный формат даты')
        case 'edit':
            print('Редактирование заметки')
            try:
                edit_id = int(input('Введите номер заметки :'))
                note_index = -1            
                for i in notes:
                    if i[0] == edit_id:                      
                        printNote(notes.index(i))
                        note_index = notes.index(i)
                        break
                if note_index == -1:
                    print('Такой заметки не существует')
                else:              
                    notes[note_index][2] = input('Введите заметку: ')
                    notes[note_index][3] = str(datetime.now().strftime("%d-%m-%Y"))
                    save()
            except:
                print('Некорректный ввод')
        case 'delete':
            print('Удаление заметки')
            try:
                delete_id = int(input('Введите номер заметки :'))
                note_index = -1            
                for i in notes:
                    if i[0] == delete_id:                      
                        printNote(notes.index(i))
                        note_index = notes.index(i)
                        break
                if note_index == -1:
                    print('Такой заметки не существует')
                else:              
                    confirm = input('Вы уверены что хотите удалить эту заметку? (y/n): ').lower()                
                    if confirm == 'y':
                        notes.pop(note_index)
                        print('Запись удалена')
            except:
                print('Некорректный ввод')
        case _:
            print('add - добавить заметку \nlist - список заметок\nsearch - поиск по дате заметки\nedit - редактировать заметку\ndelete - удалить заметку\n')





                





    


