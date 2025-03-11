from Model import *
from View import *

# Controller (Контроллер) - управляет логикой и связывает модель с представлением
def main():
    while True:
        print(get_numbers())

        choice = display_menu()

        if choice == "1":
            num_1, num_2 = get_numbers()
            plus(num_1, num_2, show_answer)
            print(show_answer(result))
        elif choice == "2":
            num_1, num_2 = get_numbers()
            minus(num_1, num_2, show_answer)
            print(show_answer(result))
        elif choice == "3":
            num_1, num_2 = get_numbers()
            multiply(num_1, num_2, show_answer)
            print(show_answer(result))
        elif choice == "4":
            num_1, num_2 = get_numbers()
            divide(num_1, num_2, show_answer)
            print(show_answer(result))
        elif choice == "0":
            print("Пока!")
            break
        else:
            show_message("Неверный выбор, попробуй снова")


main()

# # Запуск программы
# if __name__ == "__main__":
#     main()