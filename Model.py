# Model (Модель) - отвечает за данные и логику работы с ними

def plus(num_1, num_2, show_result_func):
    result = num_1 + num_2
    show_result_func(result)

def minus(num_1, num_2, show_result_func):
    result = num_1 - num_2
    show_result_func(result)

def multiply(num_1, num_2, show_result_func):
    result = num_1 * num_2
    show_result_func(result)

def divide(num_1, num_2, show_result_func):
    result = num_1 / num_2
    show_result_func(result)

