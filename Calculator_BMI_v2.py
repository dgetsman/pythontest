gender = (input("Ваш пол м/ж: "))
weight = float(input("Введите ваш вес "))
height = float(input("Введите ваш рост "))
age = int(input("Введите ваш возраст: "))
bmi = weight / (height / 100)**2
graf = ("15==================================50")
imt = round(bmi) - 15
result = graf[:imt+1] + "|" + graf[imt + 2:]
print("Ваш индекс массы тела: ", round(bmi))
print (result)
if gender == ("м") and age <= 50:
    if bmi < 20:
        print("У вас недостаток весса, нужно сходить покушать")
    elif bmi < 30:
        print("Ваш индекс массы тела в пределах нормы, поздравляю!")
    else: 
        bmi > 30
        print("У вас избыточный вес, нужно занять спортом либо пересмотреть диету")
elif gender == ("м") and age > 50:
    if bmi < 20:
        print("У вас недостаток весса, нужно сходить покушать")
    elif bmi < 30:
        print("Ваш индекс массы тела в пределах нормы, поздравляю!")
    else: 
        bmi > 30
        print("У вас избыточный вес, нужно пересмотреть диету")
elif gender == ("ж") and age <= 45:
    if bmi < 18:
        print("У вас недостаток весса, нужно сходить покушать")
    elif bmi < 27:
        print("Ваш индекс массы тела в пределах нормы, поздравляю!")
    else: 
        bmi > 27
        print("У вас избыточный вес, нужно занять спортом либо пересмотреть диету")
else: 
    gender == ("ж") and age > 45
    if bmi < 18:
        print("У вас недостаток весса, нужно сходить покушать")
    elif bmi < 27:
        print("Ваш индекс массы тела в пределах нормы, поздравляю!")
    else: 
        bmi > 27
        print("У вас избыточный вес, нужно пересмотреть диету")