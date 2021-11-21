import random
import time
import threading
from random import randint


lst = []
answer = []
abs_min = 1000000

for i in range(100000):
    lst.append(randint(-99999,99999))

lst = [-100, 2, 3, 4, -10, 6, 7, 8, 9, -11]

def min_list(num_start, num_end):
    global abs_min
    for i in range(num_start, num_end + 1):
        if lst[i] < abs_min:
            abs_min = lst[i]


if __name__ == "__main__":
    size = len(lst)
    jobs = []
    flows = 2
    n = size / flows
    start_time = time.time()
    for i in range(flows):
        thread = threading.Thread(target=min_list, args=(int(n * i), int(n * (i + 1)) - 1))
        jobs.append(thread)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    end_time = time.time()
    print("time = ", end_time - start_time)
    print("abs min = ", abs_min)
