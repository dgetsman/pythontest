a = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"
print("1. Количество символов - " , len(a))
print('2. Развернутая строка -', a[::-1])
print('3. Сделать кажде слово с заглавной -', a.title())
b = a.count("нд")
c = a.count("ам")
d = a.count("о")
print('4. Весь текст прописными -', a.lower())
print('5. Число вхождений \"нд" - ', b)
print('   Число вхождений \"ам" - ', c)
print('   Число вхождений \"о" - ', d)
print('6. Замена буквы "а" на 0 -', a.replace('о','0'))
print('Выставляем текст по центру -\n',a.center(len(a)+20))
print('7. Развернуть текст -', *reversed(a.split()))
print("8. Исходная строка -", a)