import threading as th
import time


semaphore = th.Semaphore(5)


def read_file():
    with semaphore:
        f = open('test_file.txt')
        time.sleep(5)
        f.close()
        print(th.current_thread().name)


if __name__ == "__main__":
    flows = 15
    jobs = []
    for i in range(flows):
        thread = th.Thread(target=read_file, args=())
        jobs.append(thread)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
