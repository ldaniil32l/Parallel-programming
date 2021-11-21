import random
import time
import multiprocessing
from math import sin, exp


size = 10000000
out_list = list(range(size))


def do_something(start_iter, end_iter):
    print(multiprocessing.currentProcess().getName() + str('---> starting \n'))
    for i in range(start_iter, end_iter):
        if i % 2 == 0:
            out_list[i] = sin(random.random())
        else:
            out_list[i] = exp(random.random())


if __name__ == "__main__":
    start_time = time.time()
    jobs = []
    for i in range(9):
        process = multiprocessing.Process(target=do_something, args=(int(size * i / 10), int(size * (i + 1) / 10)))
        jobs.append(process)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    end_time = time.time()
    print("Создание списка завершено")
    print("time = ", end_time - start_time)
