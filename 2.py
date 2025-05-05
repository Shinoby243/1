user_input = input("[Введите число: ")

try:
    num = int(user_input)
    if num <= 0:
        print("Ошибка: число должно быть положительным")
    else:
        parity = "четным" if num % 2 == 0 else "не является четным"
        print(f"Число {num} {parity}")
except ValueError:
    print("Ошибка: введено не число")
