'''2.Модифицировать генератор, чтобы генератор принимал
диапазон случайных чисел и чтобы последующее случайное
число лежало в диапазоне смещенном на n.
Пример: a = 1, b = 10, diff = 10'''
from time import sleep
from random import *


def create_generator(a, b, diff):
    while True:
        sleep(1)
        yield randint(a, b)
        a += diff
        b += diff


while True:
    a = create_generator(1, 10, 10)
    for y in a:
        print(y)