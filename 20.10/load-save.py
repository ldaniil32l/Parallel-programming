import threading as th
import time


condition = th.Condition()

box = []
string = 'Loading me!'


def loading():
    global string, box
    with condition:
        box.append(string)
        condition.notify()
    print(th.currentThread().getName(), "load str")
    time.sleep(1)


def unloading():
    global string, box
    with condition:
        while True:
            item = box.pop()
            if item:
                break
            condition.wait()
    print(th.currentThread().getName(), "unload str")
    time.sleep(1)


def load_unload_str():
    global string, box
    if not len(box):
        loading()
    else:
        unloading()


if __name__ == "__main__":
    flows = 7
    jobs = []
    for i in range(flows):
        thread = th.Thread(target=load_unload_str, args=())
        jobs.append(thread)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
