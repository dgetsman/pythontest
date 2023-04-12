def main(login, *args, **kwargs):
    if login != "admin":
        def dec(login):
            return
        return print("Доступ запрещен!")
    else:
        return print("Сумма на счету: 2р")
login = main(input("Введите логин: "))