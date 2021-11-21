import threading as th
from random import randint
import time

scl = 0


def scalyar(n1, n2):
    global x, y, scl
    for i in range(n1, n2):
        scl += x[i] * y[i]


if __name__ == "__main__":
    x = []
    y = []
    for i in range(10 ** 6):
        x.append(randint(-10, 10))
        y.append(randint(-10, 10))
    size = len(x)
    jobs = []
    flows = 2
    # x = [1, 2]
    # y = [0, -2]
    # scalyar(0, 2)
    n = size / flows
    for i in range(flows):
        thread = th.Thread(target=scalyar, args=(int(n * i), int(n * (i + 1)) - 1))
        jobs.append(thread)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    
    print(scl)
