a = int(input("Введите первое значение: ")) 
b = int(input("Введите второе значение: ")) 
c = int(input("Введите третье значение: ")) 
a != 0 and b != 0 and c != 0 and print(a)
a == 0 and b != 0 and c != 0 and print(b)
a != 0 and b == 0 and c != 0 and print(a)
a != 0 and b != 0 and c == 0 and print(a)
a == 0 and b != 0 and c == 0 and print(b)
a == 0 and b == 0 and c != 0 and print(c)
a + b + c == 0 and print("Введены  все нули!") or a + b + c == 0 and print("Нет нулевых значений!!!")
if a > (b + c):
    print(a - b - c)
if a < (b + c): 
    print(b + c - a)
if a > 50 and b > a or c > a:
    print("Вася")
if a > 5 and b == 7 and c == 7:
    print("Петя")
