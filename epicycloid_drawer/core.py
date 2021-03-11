import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-pastel')


def points_on_circumference(x, y, r, precision=100):
    return [(np.cos(2*np.pi / precision*(i+x) )*r,
             np.sin(2*np.pi / precision*(i+y) )*r)
            for i in np.arange(0, precision+1)]


def draw_circle(rayon=.5, speed=10, t=0, precision=100): # angle aka theta omitted
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.axis('equal')
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    scatter = ax.scatter([], [], c='red', marker='+')
    points = points_on_circumference(0, 0, rayon, precision)
    c = plt.Circle((0, 0), rayon, color='blue', fill=False)
    ax.add_artist(c)
    x = [x[0] for x in points]
    y = [y[1] for y in points]
    scatter.set_offsets(np.hstack((x[t*speed], y[t*speed])))


def draw_image(r, s=1, t=0, theta=None):
    return


def animate_image():
    return
