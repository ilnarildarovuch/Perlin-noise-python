import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
from perlin import Perlin

x_adder = 0
# Example 7: Generate 2D fBm animation
def generate_fbm_2d(width, height, scale, octaves):
    global x_adder
    fbm = np.zeros((height, width))
    for y in range(height):
        for x in range(width):
            fbm[y][x] = Perlin.fbm(x / scale + x_adder, y / scale, octave=octaves)
    x_adder += 0.1
    return fbm

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_title("2D fBm Animation")
ax.axis('off')
im = ax.imshow(generate_fbm_2d(100, 100, 10.0, 5), cmap='hot', animated=True)

def update(i):
    im.set_array(generate_fbm_2d(100, 100, 10.0, i))
    return im,

ani = matplotlib.animation.FuncAnimation(fig, update, frames=range(1, 10),
                                        interval=5, blit=True)

plt.show()