from multiprocessing import Process, Manager, Semaphore, current_process, set_start_method, get_context
import time


def read_file():
    pass


if __name__ == "__main__":
    print(get_context())
    try:
        set_start_method('spawn')
    except RuntimeError:
        print('error')
    prosc = 15
    jobs = []
    for i in range(prosc):
        proc = Process(target=read_file, args=())
        jobs.append(proc)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
