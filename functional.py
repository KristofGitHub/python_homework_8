def AddContact(fileName, abonentName, abonentNumber):
    data = open(fileName, "a")                              # Открыли файл
    data.write(abonentName + "\t")                          # Добавили имя нового контакта, табуляция
    data.write(abonentNumber + ";"+ "\n")                        # Добавили номер нового контакта, переход на новую строку
    data.close()                                            # Закрыли документ
    print("Новый контакт создан.")

def ShowAllContacts(fileName):
    print("***ТЕЛЕФОННЫЙ СПРАВОЧНИК***")
    print()
    print("СПИСОК КОНТАКТОВ:")
    data = open(fileName, "r")                              # Открыли файл
    for line in data: print(line, end="")
    data.close()                                            # Закрыли документ
    print()
    print("***КОНЕЦ СПРАВОЧНИКА***")

def SearchAbonent(fileName, abonentName):
    data = open(fileName, "r")                              # Открыли файл
    finded = 0
    count = 0
    for line in data: 
        curentName = line.split()                           # Разбиваем строку на отдельные слова и формируем из них список
        if (abonentName == curentName[0]): 
            print(line)                                     # Сравниваем с первым элементом массива (там имя)
            finded = 1
            break
        count += 1                                          # Ищем порядковый номер записи (для возможности удаления)
    if (finded == 0): print("Такой записи не существует.")
    data.close()                                            # Закрыли документ
    return count

def DeleteContact(fileName, abonentName):
    with open(fileName, "r") as file:
        lines = file.readlines()                            # Считываем все строки из файла в список
    line_to_delete = SearchAbonent(fileName, abonentName)   # Находим номер записи, которую нужно удалить     
    del lines[line_to_delete]                               # Удаляем строку из списка
    with open(fileName, "w") as file:                       # Открываем файл в режиме перезаписи
        file.writelines(lines)                              # Записываем оставшиеся строки обратно в файл
    print("Запись удалена.")

def CorrectContact(fileName, abonentName, newName, newNumber):
    with open(fileName, "r") as file:
        lines = file.readlines()                            # Считываем все строки из файла в список
    line_to_correct = SearchAbonent(fileName, abonentName)  # Находим номер записи, которую нужно отредактировать  
    lines[line_to_correct] = newName + "\t" + newNumber + ";"+ "\n"         # Редактируем строку из списка
    with open(fileName, "w") as file:                       # Открываем файл в режиме перезаписи
        file.writelines(lines)                              # Записываем строки обратно в файл
    print("Запись изменена.")