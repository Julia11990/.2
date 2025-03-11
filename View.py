# View (Представление) - отвечает за отображение и ввод данных
def display_menu():
    print("\nВыбери действие: 1 - Умножение, 2 - Деление, 3 - Сложение, 4 - Вычитание 0 - выход")
    choice = input("Введи номер действия: ")

    return choice

def get_numbers():
    num_1 = int(input("Введите 1 число: "))
    num_2 = int(input("Введите 2 число: "))
    return num_1, num_2

def show_answer(result):
    print("Ответ:", result)

def show_message(message):
    print(message)

