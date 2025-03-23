import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
from perlin import Perlin

x_adder = 0
# Example 6: Generate 2D Perlin noise animation
def generate_perlin_2d(width, height, scale):
    global x_adder
    perlin = np.zeros((height, width))
    for y in range(height):
        for x in range(width):
            perlin[y][x] = Perlin.noise(x / scale + x_adder, y / scale)
    x_adder += 0.7
    return perlin

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_title("2D Perlin Noise Animation")
ax.axis('off')
im = ax.imshow(generate_perlin_2d(100, 100, 10.0), cmap='gray', animated=True)

def update(i):
    im.set_array(generate_perlin_2d(100, 100, 10.0))
    return im,

ani = matplotlib.animation.FuncAnimation(fig, update, frames=range(1, 10),
                                        interval=1, blit=True)

plt.show()