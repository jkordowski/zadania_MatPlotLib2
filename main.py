import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

z = np.linspace(0, 2*np.pi)
x = np.sin(z)
y = 2*np.cos(z)
ax.plot(x, y, z)
ax.legend()
plt.show()
