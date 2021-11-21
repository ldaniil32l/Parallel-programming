import random
import time
import threading
from random import randint


lst = []


for i in range(30):
    lst.append(randint(-999,999))


def sort_buble(num_start, num_end):
    global lst
    print(threading.currentThread().getName())

    for i in range(num_end, num_start, -1):
        for j in range(0, i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


if __name__ == "__main__":
    size = len(lst)
    jobs = []
    flows = 5
    n = size / flows
    start_time = time.time()
    for j in range(n + 1):
        for i in range(flows):
            thread = threading.Thread(target=sort_buble, args=(int(n * i), int(n * (i + 1))))
            jobs.append(thread)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()

    end_time = time.time()
    print("time = ", end_time - start_time)
    print("sort list = ", lst)
