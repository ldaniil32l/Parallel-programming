import numpy as np
import matplotlib.pyplot as plt
import threading as th
import time


def render_point(n1, n2):
    global arr_ppoins
    ip = n1
    for p in range(n1, n2):
        calc_q(arr_ppoins[p], ip)
        ip += 1


def calc_q(p, ip):
    global image, qmin, qmax, qpoints, infinity_border, max_iterations
    for iq, q in enumerate(np.linspace(qmin, qmax, qpoints)):
        c = p + 1j * q
        z = 0
        for k in range(max_iterations):
            z = z ** 2 + c
            if abs(z) > infinity_border:
                image[ip, iq] = 1
                break


pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2
ppoints, qpoints = 200, 200
max_iterations = 300
infinity_border = 100
image = np.zeros((ppoints, qpoints))

arr_ppoins = np.linspace(pmin, pmax, ppoints)
N = len(arr_ppoins)

start_time = time.time()

jobs = []
flows = 10
n = N / flows
for i in range(flows):
    thread = th.Thread(target=render_point, args=(int(n * i), int(n * (i + 1)) ))
    jobs.append(thread)
for j in jobs:
    j.start()
for j in jobs:
    j.join()

end_time = time.time()


plt.xticks([])
plt.yticks([])

plt.imshow(-image.T, cmap='Greys')

plt.text(0, 1, f"parallel, time: {end_time - start_time}", backgroundcolor='white', color='black')

plt.show()