import numpy as np
import matplotlib.pyplot as plt
import threading as th
import time


pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2
ppoints, qpoints = 200, 200
max_iterations = 300
infinity_border = 100
image = np.zeros((ppoints, qpoints))

start_time = time.time()

for ip, p in enumerate(np.linspace(pmin, pmax, ppoints)):
    for iq, q in enumerate(np.linspace(qmin, qmax, qpoints)):
        c = p + 1j * q
        z = 0
        for k in range(max_iterations):
            z = z ** 2 + c
            if abs(z) > infinity_border:
                image[ip, iq] = 1
                break

end_time = time.time()


plt.xticks([])
plt.yticks([])

plt.imshow(-image.T, cmap='Greys')

plt.text(0, 1, f"serial, time: {end_time - start_time}", backgroundcolor='white', color='black')

plt.show()