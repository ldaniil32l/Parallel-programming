from multiprocessing import Process, Manager
from random import randint
import time


def scalyar(n1, n2, x, y, lst):
    scl_loc = 0
    for i in range(n1, n2):
        scl_loc += x[i] * y[i]
    lst.append(scl_loc)


if __name__ == "__main__":
    manager = Manager()
    lst = manager.list()
    x = []
    y = []
    for i in range(10 ** 4):
        x.append(randint(-10, 10))
        y.append(randint(-10, 10))
    size = len(x)
    jobs = []
    prcs = 100
    # x = [1, 2, 1]
    # y = [0, -2, 3]
    # size = 3
    # scalyar(0, 2)
    n = size / prcs
    for i in range(prcs):
        proc = Process(target=scalyar, args=(int(n * i), int(n * (i + 1)), x, y, lst))
        jobs.append(proc)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    scl = 0
    for num in lst:
        scl += num
    print(scl)
