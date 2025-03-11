# View (Представление) - отвечает за отображение и ввод данных
def display_menu():
    print("\nВыбери действие: 1 - Умножение, 2 - Деление, 3 - Сложение, 4 - Вычитание 0 - выход")
    choice = input("Введи номер действия: ")

    return choice

def get_numbers():
    num_1 = input("Введите 1 число: ")
    user_input1 = num_1

    if user_input1.isdigit():
        number1 = int(user_input1)  # Преобразование в целое число
        print("Вы ввели число:", number1)
    else:
        print("Ошибка: введено не число.")
    num_2 = input("Введите 2 число: ")
    user_input2 = num_2

    if user_input2.isdigit():
        number2 = int(user_input1)  # Преобразование в целое число
        print("Вы ввели число:", number2)
    else:
        print("Ошибка: введено не число.")

def show_answer(result):
    print("Ответ:", result)

def show_message(message):
    print(message)

