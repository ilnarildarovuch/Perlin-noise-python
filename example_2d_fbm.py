import numpy as np
import matplotlib.pyplot as plt
from perlin import Perlin

Perlin.seed(214)

octaves = 5
# Example 5: Generate fBm for 2D
def generate_fbm_2d(width, height, scale, octaves):
    fbm = np.zeros((height, width))
    for y in range(height):
        for x in range(width):
            fbm[y][x] = Perlin.fbm(x / scale, y / scale, octave=octaves)
    return fbm

width, height = 100, 100
scale = 10.0
fbm_2d = generate_fbm_2d(width, height, scale, octaves)

plt.figure(figsize=(6, 6))
plt.imshow(fbm_2d, cmap='hot')
plt.title("2D fBm")
plt.axis('off')
plt.show()