import numpy as np
import matplotlib.pyplot as plt
from perlin import Perlin

# Example 4: Generate fBm for 1D
x_values = np.linspace(0, 5, 100)
octaves = 5
fbm_values_1d = [Perlin.fbm(x, octave=octaves) for x in x_values]

plt.figure(figsize=(10, 4))
plt.plot(x_values, fbm_values_1d, color='orange')
plt.title("1D fBm (Fractional Brownian Motion)")
plt.xlabel("x")
plt.ylabel("fBm Value")
plt.grid()
plt.show()