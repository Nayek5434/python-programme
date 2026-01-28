import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 100)
e = np.exp(1)
p = (15000 * (1 + t)) / (15 + e)

plt.plot(t, p)
plt.title("Bacteria Population vs Time")
plt.xlabel("Time (hours)")
plt.ylabel("Population")
plt.show()
