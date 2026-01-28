import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
plt.plot(x, np.sin(x), label='Sine')
plt.plot(x, np.cos(x), label='Cosine')
plt.plot(x, x**2, label='Polynomial')
plt.plot(x, np.exp(x), label='Exponential')
plt.legend()
plt.title("Mathematical Curves")
plt.show()