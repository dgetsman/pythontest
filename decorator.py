def decorator(func):
    # @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        user = input("Введите логин: ")
        if user == 'admin':
            valadue = func(*args, **kwargs)
        else:
            return print('Доступ запрещен!')
        # Do something after
    return wrapper_decorator

@decorator
def main():
    print("Сумма на счету 2р")
main()