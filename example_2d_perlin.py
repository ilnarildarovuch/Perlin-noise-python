import numpy as np
import matplotlib.pyplot as plt
from perlin import Perlin

# Example 2: Generate 2D Perlin noise
def generate_2d_noise(width, height, scale):
    noise = np.zeros((height, width))
    for y in range(height):
        for x in range(width):
            noise[y][x] = Perlin.noise(x / scale, y / scale)
    return noise

width, height = 100, 100
scale = 10.0
noise_2d = generate_2d_noise(width, height, scale)

plt.figure(figsize=(6, 6))
plt.imshow(noise_2d, cmap='gray')
plt.title("2D Perlin Noise")
plt.axis('off')
plt.show()

