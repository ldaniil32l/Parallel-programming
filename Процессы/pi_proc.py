from multiprocessing import Process, Manager
import time


def search_pi(n1, n2, N, lst):
    pi_local = 0
    for i in range(n1, n2):
        xi = (i + 0.5) / N
        pi_local += (4 / (1 + xi ** 2)) / N
    lst.append(pi_local)


if __name__ == "__main__":
    manager = Manager()
    lst = manager.list()
    jobs = []
    N = 10 ** 6
    procs = 10 ** 2
    n = N / procs
    for i in range(procs):
        proc = Process(target=search_pi, args=(int(n * i), int(n * (i + 1)), N, lst))
        jobs.append(proc)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    pi = 0
    for num in lst:
        pi += num
    print(pi)
