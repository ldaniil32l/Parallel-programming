from multiprocessing import Process, Manager, Condition, current_process
import time

condition = Condition()


def loading(string, box):
    with condition:
        box.append(string)
        condition.notify()
    print(current_process().name, "load str")
    time.sleep(1)


def unloading(string, box):
    with condition:
        while True:
            item = box[0]
            box[:] = []
            if item:
                break
            condition.wait()
    print(current_process().name, "unload str")
    time.sleep(1)


def load_unload_str(string, box):
    if not len(box):
        loading(string, box)
    else:
        unloading(string, box)


if __name__ == "__main__":
    manager = Manager()
    box = manager.list()
    print(current_process().name)

    string = 'Loading me!'

    procs = 7
    jobs = []
    for i in range(procs):
        proc = Process(target=load_unload_str, args=(string, box))
        jobs.append(proc)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
