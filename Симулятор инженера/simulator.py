import threading as th
from random import randint
from datetime import time, timedelta, datetime
from queue import Queue
from time import sleep

condition = th.Condition()
queue = Queue()


def random_time_repair():
    return randint(10, 51)


# def loading():
#     global string, box
#     with condition:
#         box.append(string)
#         condition.notify()
#     print(th.currentThread().getName(), "load str")
#     time.sleep(1)


# def unloading():
#     global string, box
#     with condition:
#         while True:
#             item = box.pop()
#             if item:
#                 break
#             condition.wait()
#     print(th.currentThread().getName(), "unload str")
#     time.sleep(1)


def repair_order():
    # время прихода клиента
    hour = randint(0, 12)
    minuts
    sleep(randint(0, 5))

    print("1")


def work():
    pass


start_day = datetime(year = 2021, month = 11, day = 23, hour = 9, minute = 0)
print(f"Start work-day, {start_day.strftime('%X')}")

current_time = start_day + timedelta(minutes=30)
print(f"Time, {current_time.strftime('%X')}")

engineer = th.Thread(target=work, args=())
engineer.start()

# TODO: вставить в завершение рабочего дня инженера: что-то

clients = []
count_clients = 100

for i in range(count_clients):
    client = th.Thread(target=repair_order, args=())
    clients.append(client)

for client in clients:
    if queue.qsize() < 3:
        queue.put(client)
    # client.start()

print(queue.qsize())

queue.get().start()
queue.get().start()
queue.get().start()

# for client in clients:
#     client.join()

end_day = datetime(year = 2021, month = 11, day = 23, hour = 21, minute = 0)
print(f"End work-day, {end_day.strftime('%X')}")
