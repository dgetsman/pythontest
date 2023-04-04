a = float(input("Введите ваш вес "))
b = float(input("Введите ваш рост "))
c = a / (b / 100)**2
graf = ("15==============30")
imt = round(c) - 15
result = graf[:imt+1] + "|" + graf[imt + 2:]
print("Ваш индекс массы тела: ", round(c))
print (result)