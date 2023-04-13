import os
login = {}
login['Dmitry'] = {'Рост - ': 188, 'Вес - ': 80, 'BMI - ': 23},
while True:
    menu = input("Вывести список пользователей - L \nПосмотреть информацию о пользователе - R \nИзменить\
 информацию о пользователе - U \nУдалить выбранного пользователя - D\
\nДобавить пользователя - C \nВыход - Q\nВыберите действие: ")
    def start(*args, **kwargs):
        if menu == 'L':
            os.system('CLS')
            return print(login)
        elif menu == 'R':
            key = input('Введите имя пользователя: ')
            if key not in login:
                os.system('CLS')
                print('Нет такого пользователя!')
            else:
                os.system('CLS')
                return print(login[key])
        elif menu == 'U':
            os.system('CLS')
            key = input('Введите имя пользователя: ')
            if key not in login:
                os.system('CLS')
                print('Нет такого пользователя!')
            else:
                height = int(input('Введите рост: '))
                weight = int(input('Введите вес: '))
                bmi = int(weight / (height / 100)**2)
                login[key] = {'Рост - ': height, 'Вес - ': weight, 'BMI - ': round(bmi)}
                os.system('CLS')
                return login[key]
        elif menu == 'D':
            os.system('CLS')
            key = input('Введите имя пользователя которого хотите удалить: ')
            if key not in login:
                os.system('CLS')
                print('Нет такого пользователя!')
            else:
                del(login[key])
                os.system('CLS')
                return print('Пользователь удален!')
        elif menu == 'C':
            os.system('CLS')
            key = input('Введите имя нового пользователя: ')
            height = int(input('Введите рост: '))
            weight = int(input('Введите вес: '))
            bmi = int(weight / (height / 100)**2)
            login[key] = {'Рост - ': height, 'Вес - ': weight, 'BMI - ': round(bmi)}
            os.system('CLS')
            return login[key]
        else:
            os.system('CLS')
            return print('Некоректный ввод!')
    if menu == 'Q':
        break
    start()