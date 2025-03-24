import numpy as np
import matplotlib.pyplot as plt
from perlin import Perlin

Perlin.seed(214)

# Example 1: Generate 1D Perlin noise
x_values = np.linspace(0, 5, 100)
noise_values_1d = [Perlin.noise(x) for x in x_values]

plt.figure(figsize=(10, 4))
plt.plot(x_values, noise_values_1d)
plt.title("1D Perlin Noise")
plt.xlabel("x")
plt.ylabel("Noise Value")
plt.grid()
plt.show()

