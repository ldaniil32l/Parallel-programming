from multiprocessing import Process, Manager, Semaphore, current_process, set_start_method, get_context
import time


def read_file(semaphore):
    with semaphore:
        f = open('test_file.txt',encoding='utf-8')
        for i in range(100000):
            word = f.read(10 ** 6)
            word += word
        print(semaphore)
        time.sleep(3)
        f.close()
        print(current_process().name)


if __name__ == "__main__":
    semaphore = Semaphore(5)

    prosc = 15
    jobs = []
    for i in range(prosc):
        proc = Process(target=read_file, args=(semaphore,))
        jobs.append(proc)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
