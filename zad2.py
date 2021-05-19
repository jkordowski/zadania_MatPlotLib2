import numpy as np
import matplotlib.pyplot as plt

np.random.seed(194526)


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 20

for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5), ('c', '*', -40, -10),
                          ('g', 'P', -25, -5), ('m', 'd', -60, -30)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('oś X')
ax.set_ylabel('oś Y')
ax.set_zlabel('oś Z')
plt.show()
