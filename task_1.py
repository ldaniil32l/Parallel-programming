import random
import time
from math import sin, exp


size = 10000000
out_list = list(range(size))


def do_something(start_iter, end_iter):
    for i in range(start_iter, end_iter):
        if i % 2 == 0:
            out_list[i] = sin(random.random())
        else:
            out_list[i] = exp(random.random())


if __name__ == "__main__":
    start_time = time.time()
    for j in range(9):
        do_something(int(size * j / 10), int(size * (j + 1) / 10))
    end_time = time.time()
    print("Создание списка завершено")
    print("time = ", end_time - start_time)
