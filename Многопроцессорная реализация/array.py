import multiprocessing as mp
from random import randint
import numpy as np
from time import sleep


def worker(arr, q):
    while q.qsize() != 0:
        num = int(mp.current_process().name[-1])
        if num == q.get():
            print(mp.current_process().name, arr[q.qsize() + 1])
            sleep(2)


if __name__ == "__main__":
    arr = np.array(range(10 ** 4))
    q = mp.Queue()
    jobs = []
    procs = 4
    for i in range(1, 10 ** 4):
        if i % 4 == 0:
            q.put(4)
        else:
            q.put(i % 4)
    for i in range(procs):
        p = mp.Process(target=worker, args=(arr, q))
        p.start()
        jobs.append(p)
    for j in jobs:
        j.join()
