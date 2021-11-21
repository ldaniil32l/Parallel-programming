import random
import time
import threading
import random


lst = list(range(0, 10001))
answer = []
s = 0

def summ(num_start, num_end):
    global s
    l = 0
    for i in range(num_start, num_end + 1):
        l += lst[i]
    s += l


if __name__ == "__main__":
    size = 10000
    jobs = []
    flows = 100
    n = size / flows
    start_time = time.time()
    for i in range(flows):
        thread = threading.Thread(target=summ, args=(int(n * i), int(n * (i + 1))))
        jobs.append(thread)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()


    end_time = time.time()
    print("time = ", end_time - start_time)
    print("summ 1:10000 = ", s)
    u = (1 + 10000) * 5000
    print(u)
