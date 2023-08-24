# ЗАДАЧА (на сегодня одна). Создать телефонную книгу, которая будет импортировать и экспортировать данные.
# Вывод всех данных, ввод данных (сохранение), поиск по фамилии.
''' 
СТРУКТУРА ПРОЕКТА
Будет содержать три отдельных элемента (три файла, принцип модульности):
    1. Интерфейс - все для взаимодействия программы с пользователем.
    2. Работа с файлом (БД) - функция чтения и записи из\в файл.
    3. Алгоритм работы программы.
'''
import functional

path ="phone book.txt"
try:
    file = open(path, "r")                                  # Если файл существует, то открываем его просто эркой
except IOError:
    print("Создан новый справочник - phone book.txt")       # Если не существует и выдает ошибку - создаем вэшкой
    file = open(path, "w")
finally:
    file.close()                                            # В конце - закрываем файл

userChoise = 5
while (userChoise != 0):
    print()
    print("ТЕЛЕФОННЫЙ СПРАВОЧНИК: МЕНЮ")
    print("1 - Посмотреть весь справочник")
    print("2 - Поиск по имени")
    print("3 - Создать запись")
    print("4 - Удалить запись")
    print("5 - Редактировать запись")
    print("0 - Выход")
    print("-------------")
    print()
    userChoise = int(input("Выберите действие: "))
    print()
    if (userChoise == 1): functional.ShowAllContacts(path)
    if (userChoise == 2):
        findingName = str(input("Введите имя абонента: "))
        num = functional.SearchAbonent(path, findingName)
    if (userChoise == 3):
        newName = str(input("Введите имя абонента: "))
        newNumber = str(input("Введите номер абонента: "))
        functional.AddContact(path, newName, newNumber)
    if (userChoise == 4):
        deletingName = str(input("Введите имя удаляемого абонента: "))
        functional.DeleteContact(path, deletingName)
    if (userChoise == 5):
        deletingName = str(input("Введите имя удаляемого абонента: "))
        newName = str(input("Введите измененное имя абонента: "))
        newNumber = str(input("Введите измененный номер абонента: "))
        functional.CorrectContact(path, deletingName, newName, newNumber)
    if (userChoise == 0): print("Работа закончена.")