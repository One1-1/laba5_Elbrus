#part A - 19    part B - 24, 49, 74 part C - 19, 26, 42

"""
Главный модуль программы
Осуществляет выполнение выбранной из меню задачи, посредством вызова
соответствующей подпрограммы
Перед вызовом запрашивает нужные исходные данные подпрограммы
"""

from lab5.my_library import task6_1, task6_2, task6_3, task6_4, task6_5, task6_6, task6_7


def menu():
    """
    Функция предлагает выбор номера задания\n
    :param : нет передаваемых параметров
    :return: choice_task - выбранный номер задания
    """

    choice_task = int(input('Выберите номер задания в лабороторной работе: '))

    return choice_task

if __name__ == '__main__':
    while True:
        choice = menu()

        match choice:

            case 1:
                s1 = input('Введите первую строку: ')
                s2 = input('Введите вторую строку: ')

                print(task6_1(s1, s2))

            case 2:
                text = input('Введите текст: ')
                word = input('Введите слово, которое надо составить: ')

                task6_2(text, word)

            case 3:
                text = input("Введите текст: ")
                length = int(input("Введите длину слов для удаления: "))
                print(task6_3(text, length))

            case 4:
                s = input('Введите строку: ')
                print(task6_4(s))

            case 5:
                date_input = input("Введите дату в формате YYYY-MM-DD или YY-MM-DD: ")
                task6_5(date_input)

            case 6:
                input_string = input('Введите строку: ')
                task6_6(input_string)

            case 7:
                text = input("Введите текст: ")
                print(task6_7(text))

            case _:
                    break
        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break

