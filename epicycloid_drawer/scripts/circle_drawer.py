#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:02:50 2020

@author: qd
source https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c
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

points = points_on_circumference(0, 0, RAYON, N_POINTS)

def init():
    c = plt.Circle((0, 0), RAYON, color='blue', fill=False)
    ax.add_artist(c)
    return scatter, c

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
ax.add_artist(c)
x = [x[0] for x in points]
y = [y[1] for y in points]
scatter.set_offsets(np.hstack((x[1*SPEED], y[1*SPEED])))
fig.savefig('test_speed_1circle_t1.png')
"""
