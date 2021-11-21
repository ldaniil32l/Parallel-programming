import threading as th
import time


condition = th.Condition()

string1 = 'Loading me! - 1'
string2 = 'Loading me! - 2'
string3 = 'Loading me! - 3'
string4 = 'Loading me! - 4'
string0 = 'Loading me! - 0'

box = [string0, string1, string2, string3, string4]


class MyThread(th.Thread):
    def __init__(self, thID):
        super().__init__(group=None, target=unloading, name=None, args=(), kwargs={}, daemon=None)
        self.id = thID


def unloading():
    global string, box
    item = 'None'
    for i in range(len(box)):
        if i == th.currentThread().id:
            item = box[i]
    print('Thread -', th.currentThread().id, 'unload sring:', item)


if __name__ == "__main__":
    flows = 5
    jobs = []
    for i in range(flows):
        thread = MyThread(i)
        jobs.append(thread)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
