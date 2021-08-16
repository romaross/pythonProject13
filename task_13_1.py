'''Написать калькулятор. Программа должна содержать 4 функции
принимающие два аргумента и возвращающие результаты сложения,
вычитания, умножения и деления. Реализовать пользовательский
интерфейс с бесконечным циклом. Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(task_13_1.py, func.py, ui_func.py
exceptions.py). [my-oop-t05]'''

""" Decorator function for simple printing """


class Math:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2


def sum(self):
    return self.arg1 + self.arg2


a = Math(5, 6)
sum_1 = sum(a)
print(sum_1)


def printable2args(func):
    def wrapper(arg1, arg2):
        result = func(arg1, arg2)
        if func.__name__ == 'addition':
            print('+')
        elif func.__name__ == 'substruction':
            print('-')
        elif func.__name__ == 'multiplication':
            print('*')
        elif func.__name__ == 'division':
            print('/')
        print(' Result of operation (', func.__name__, '): ', result)
        return result

    return wrapper


""" Simple addition """


@printable2args
def addition(a, b):
    return a + b


""" Simple subtruction """


@printable2args
def subtruction(a, b):
    return a - b


""" Simple multiplication """


@printable2args
def multiplication(a, b):
    return a * b


""" Simple division """


@printable2args
def division(a, b):
    # if b == 0:
    #    return 1
    # else:
    return a / b


""" Test function """


def main_func():
    try:
        x = float(input('Input first value:'))
        y = float(input('Input second value:'))

    except:
        print('Incorrect values')
    list1 = [addition, subtruction, multiplication, division]
    for value_func in list1:
        try:
            value_func(x, y)
        except ZeroDivisionError:
            print(' Can not divide by zero ')


if __name__ == '__main__':
    main_func()
