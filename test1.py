while True:
    menu = input("Вывести список пользователей - L \nПосмотреть информацию о пользователе - R \nИзменить\
 информацию о пользователе - U \nУдалить выбранного пользователя - D\
\nДобавить пользователя - C \nВыход - Q\n")
    login = {}
    login[1] = {'Name - ': 'Dmitry', 'Рост - ': 188, 'Вес - ': 80, 'BMI - ': 23},
    if menu == "Q":
        break
    elif menu == "L":
        print(login)
    elif menu == "R":
        user_info = int(input("Введите номер пользователя для информации: "))
        print(login[user_info])
    elif menu == "U":
        user_change = int(input("Выберите номер пользователя для изменения: "))
        name = input("Введите имя: ")
        height = int(input("Введите рост: "))
        weight = int(input("Введите вес: "))
        bmi = int(weight / (height / 100)**2)
        login[user_change] = {'Name - ': name, 'Рост - ' : height,'Вес - ': weight,'BMI - ': round(bmi)}
    elif menu == "D":
        user_del = input("Введиет имя пользователя которого хотите удалить: ")
        del(login[user_del])
    elif menu == "C":
        user_add = input("Выберите имя пользователя для добавления: ")
        height = int(input("Введите рост: "))
        weight = int(input("Введите вес: "))
        bmi = int(weight / (height / 100)**2)
        login[user_add] = {'Рост - ': height,'Вес - ': weight,'BMI - ': round(bmi)}
    else:
        print("Некорректный ввод")