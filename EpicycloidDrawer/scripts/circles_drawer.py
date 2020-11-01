ch#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:15:03 2020

@author: qd
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')

N_POINTS = 100
RAYON = .5
ANGLE = 0
SPEED = 10
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.axis('equal')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
scatter = ax.scatter([], [], c='red', marker='+')

def points_on_circumference(x, y, r, precision=100):
    return [(np.cos(2*np.pi / precision*(i+x) )*r,
             np.sin(2*np.pi / precision*(i+y) )*r)
            for i in np.arange(0, precision+1)]

def current_point_on_circle(xy: tuple, t, r, speed=1,
                            precision=100):
    center_x, center_y = xy[0], xy[1]
    return (np.cos(2*np.pi/precision*(t*speed + center_x) )*r,
            np.sin(2*np.pi/precision*(t*speed + center_y) )*r)

points = points_on_circumference(0, 0, RAYON, N_POINTS)

def init():
    c = plt.Circle((0, 0), RAYON, color='blue', fill=False)
    c2 = plt.Circle(points[0], RAYON/2, color='blue', fill=False)
    ax.add_artist(c)
    ax.add_artist(c2)
    scatter.set_offsets(np.hstack(points[0]))
    return scatter, c, c2

def animate(i):
    x = [x[0] for x in points]
    y = [y[1] for y in points]
    scatter.set_offsets(np.hstack((x[i%N_POINTS], y[i%N_POINTS])))
    return scatter,

anim = FuncAnimation(fig, animate, init_func=init,
                     frames=200, interval=20, blit=True)

# anim.save('circle_around2.gif', writer='imagemagick')
"""
c = plt.Circle((0, 0), RAYON, color='blue', fill=False)
ax.add_artist(c)
x = [x[0] for x in points]
y = [y[1] for y in points]
scatter.set_offsets(np.hstack((x[0], y[0])))
fig.savefig('test_speed_1circle.png')
"""
"""
c = plt.Circle((0, 0), RAYON, color='blue', fill=False)
center_circle2 = current_point_on_circle((0, 0), 1, RAYON)
c2 = plt.Circle(center_circle2, RAYON/2, color='blue', fill=False)
ax.add_artist(c2)
ax.add_artist(c)
x = [x[0] for x in points]
y = [y[1] for y in points]
scatter.set_offsets(np.hstack((x[1*SPEED], y[1*SPEED])))
scatter.set_offsets(np.hstack(center_circle2))
fig.savefig('test_twocircles_t1.png')
"""
