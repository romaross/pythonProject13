'''Создать бесконечный генератор случайных чисел.
Использовать в генераторе временную задержку
 from time import sleep
time.sleep(1)'''

from time import sleep
from random import*

def create_generator():
    while True:
        sleep(1)
        x = randint(0, 10000)
        yield x


while True:
    a = create_generator()
    for y in a:
        print(y)