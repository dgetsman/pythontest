users = {}
users[1] = "1. Имя - Dmitry , Рост - 188 , Вес - 80 , BMI - 23"
users[2] = "2. Имя - Anton , Рост - 165 , Вес - 64 , BMI - 24"
import os

def show_users():
    os.system('CLS')
    i = len(users)
    for i in users:
        print(users[i])
    _ = input(' ')
    os.system('CLS')
    return main()

def user_info():
    os.system('CLS')
    id = int(input('Введите id пользователя: '))
    print(users[id])
    _ = input(' ')
    os.system('CLS')
    return main()

def change_info():
    os.system('CLS')
    id = int(input("Введите id пользователя для изменений: "))
    name = input('Введиет имя пользователя: ')
    height = input('Введите рост: ')
    weight = input('Введите вес: ')
    bmi = (int(weight) / (int(height) / 100)**2)
    users[id] = f'{str(id)}. Имя - {name}, Рост - {height}, Вес - {weight}, BMI - {str(round(bmi))}'
    print("Пользователь изменен!")
    _ = input(' ')
    os.system('CLS')
    return main()

def del_user():
    os.system('CLS')
    id = int(input("Введите id пользователя которого хотите удалить: "))
    del(users[id])
    print("Пользователь удален!")
    _ = input(' ')
    os.system('CLS')
    return main()

def add_user():
    os.system('CLS')
    id = len(users)
    name = input("Введите имя пользователя: ")
    height = input("Введите рост: ")
    weight = input("Введите вес: ")
    bmi = int(weight) / (int(height) / 100)**2
    users[id + 1] = f'{str(id + 1)}. Имя - {name}, Рост - {height}, Вес - {weight}, BMI - {str(round(bmi))}'
    print("Пользователь добавлен!")
    _ = input(' ')
    os.system('CLS')
    return main()

def main():
    os.system("CLS")
    menu = input("1. Вывести список пользователей \n2. Посмотреть информацию о пользователе \n3. Изменить\
 информацию о пользователе \n4. Удалить выбранного пользователя \
\n5. Добавить пользователя \n6. Выход \nВыберите действие: ")
    while True:
        if menu == "1":
            return show_users()
        elif menu == "2":
            return user_info()
        elif menu == "3":
            return change_info()
        elif menu == "4":
            return del_user()
        elif menu == "5":
            return add_user()
        elif menu == "6":
            break
main()