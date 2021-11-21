import random
import time
import threading
import random

lst = []


def search_simple_num(area_start, area_end):
    print(threading.currentThread().getName())
    for i in range(area_start, area_end + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)


if __name__ == "__main__":
    size = 10000
    jobs = []
    flows = 100
    n = size / flows
    start_time = time.time()
    for i in range(flows):
        if i != 0:

            thread = threading.Thread(target=search_simple_num, args=(int(n * i), int(n * (i + 1))))
        else:
            thread = threading.Thread(target=search_simple_num, args=(2, int(n * (i + 1))))
        jobs.append(thread)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()


    end_time = time.time()

    print("time = ", end_time - start_time)
    print("the number of prime numbers - ", len(lst))
    for i in range(5):
        print(lst[random.randint(0, len(lst))])
