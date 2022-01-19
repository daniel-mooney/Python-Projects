from matplotlib import pyplot as plt
import numpy as np
import math

amp = 1
decay = 0.5
phase = 0
ang_freq = 7
offset = 16

f = lambda x: amp * math.exp(-decay * x) * (math.cos(ang_freq*x + phase) + math.sin(ang_freq*x + phase)) + offset

step = 0.01
x = np.arange(0, 10 + step, step)

y = np.array(list(map(f, x)))
w = np.full(len(x), offset)

plt.plot(x, y, label = "motor speed")
plt.plot(x, w, color = "red", label = "req. speed")
plt.ylabel("Motor speed (RPM)")
plt.xlabel("time (s)")
plt.title("Motor Speed vs Time")
plt.legend()
plt.show()