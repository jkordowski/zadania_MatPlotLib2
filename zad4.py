import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=plt.figaspect(0.5))
ax1 = fig.add_subplot(2, 3, 1, projection='3d')
ax2 = fig.add_subplot(2, 3, 2, projection='3d')
ax3 = fig.add_subplot(2, 3, 3, projection='3d')
ax4 = fig.add_subplot(2, 3, 4, projection='3d')
ax5 = fig.add_subplot(2, 3, 5, projection='3d')
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top, color='r', shade=True)
ax2.bar3d(x, y, bottom, width, depth, top, color='m', shade=False)
ax3.bar3d(x, y, bottom, width, depth, top, color='y', shade=True)
ax4.bar3d(x, y, bottom, width, depth, top, color='g', shade=False)
ax5.bar3d(x, y, bottom, width, depth, top, color='c', shade=True)
plt.show()