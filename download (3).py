while True:
    user_input = input("Введите число: ").strip()
    if user_input.lower() == "exit":
        print("Выход из программы...")
        break
    cleaned_input = user_input.lstrip('+-')
    if cleaned_input.isdigit():
        num_length = len(cleaned_input)
        print(f"В этом числе {num_length} цифры.")
    else:
        print("Ошибка: данные не являются числом.")