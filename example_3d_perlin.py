import numpy as np
from perlin import Perlin

Perlin.seed(214)

# Example 3: Generate 3D Perlin noise
def generate_3d_noise(x_size, y_size, z_size, scale):
    noise = np.zeros((z_size, y_size, x_size))
    for z in range(z_size):
        for y in range(y_size):
            for x in range(x_size):
                noise[z][y][x] = Perlin.noise(x / scale, y / scale, z / scale)
    return noise

x_size, y_size, z_size = 10, 10, 10
scale = 5.0
noise_3d = generate_3d_noise(x_size, y_size, z_size, scale)

print("3D noise generated with shape:", noise_3d.shape)

