import matplotlib.pyplot as plt
import numpy as np

u = float(input("Enter initial velocity (u): "))
a = float(input("Enter acceleration (a): "))
t = np.linspace(0, 10, 100)

v = u + a * t
s = u * t + 0.5 * a * t**2
s_v = (v**2 - u**2) / (2 * a)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(t, v)
plt.title("Velocity vs Time")
plt.xlabel("Time")
plt.ylabel("Velocity")

plt.subplot(1, 3, 2)
plt.plot(t, s)
plt.title("Distance vs Time")
plt.xlabel("Time")
plt.ylabel("Distance")

plt.subplot(1, 3, 3)
plt.plot(v, s_v)
plt.title("Distance vs Velocity")
plt.xlabel("Velocity")
plt.ylabel("Distance")

plt.tight_layout()
plt.show()