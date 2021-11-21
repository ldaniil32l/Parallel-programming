import random
import time
import threading
from random import randint


lst = []

for i in range(30):
    lst.append(randint(-999,999))


def sort_buble():
    global lst
    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]


if __name__ == "__main__":
    size = len(lst)
    jobs = []
    flows = 5
    n = size / flows
    start_time = time.time()
    for i in range(flows ** 2):
        thread = threading.Thread(target=sort_buble, args=())
        jobs.append(thread)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()

    end_time = time.time()
    print("time = ", end_time - start_time)
    print("sort list = ", lst)
