import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 100)
m = 60 / (t + 2)

plt.plot(t, m)
plt.title("Mass vs Time")
plt.xlabel("Time (hours)")
plt.ylabel("Mass (m)")
plt.show()