age_input = input("Введите ваш возраст: ")
try:
    age = int(age_input)
    if age < 0:
        print("Ошибка: возраст не может быть отрицательным!")
    else:
        if age >= 18:
            print("Вы совершеннолетний.")
        else:
            print("Вы несовершеннолетний.")
except ValueError:
    print("Ошибка: введено не число!")