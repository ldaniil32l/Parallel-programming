import threading as th
from random import randint
import time


pi = 0


def search_pi(n1, n2):
    global pi
    for i in range(n1, n2):
        xi = (i + 0.5) / N
        pi += (4 / (1 + xi ** 2)) / N
    # print(pi)


if __name__ == "__main__":
    jobs = []
    N = 10 ** 6
    flows = 10 ** 2
    n = N / flows
    for i in range(flows):
        thread = th.Thread(target=search_pi, args=(int(n * i), int(n * (i + 1))))
        jobs.append(thread)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print(pi)
