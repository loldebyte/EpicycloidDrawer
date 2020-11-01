import numpy as np
from matplotlib import pyplot as plt
import math
plt.style.use('seaborn-pastel')


# TODO: rewrite with a phase argument
# return points starting with point at phase
def points_on_circumference(x, y, r, precision=100):
    return [((np.cos(2*np.pi / precision*i))*r + x,
             (np.sin(2*np.pi / precision*i))*r + y)
            for i in np.arange(0, precision+1)]


def current_point_on_circle(xy: tuple, t, r, speed=1, precision=100):
    center_x, center_y = xy[0], xy[1]
    return (np.cos(2*np.pi/precision*(t*speed + center_x))*r,
            np.sin(2*np.pi/precision*(t*speed + center_y))*r)


N_POINTS = 100
RAYON = .5
ANGLE = 0
SPEED = 1
PHASE = math.radians(30)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.axis('equal')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
scatter = ax.scatter([], [], c='red', marker='+')

points = points_on_circumference(0, 0, RAYON, N_POINTS)

c = plt.Circle((0, 0), RAYON, color='blue', fill=False)
center_circle2 = current_point_on_circle((0, 0), 1, RAYON)
c2 = plt.Circle(center_circle2, RAYON/2, color='blue',
                fill=False)
ax.add_artist(c2)
ax.add_artist(c)
c2_points = points_on_circumference(center_circle2[0],
                                    center_circle2[1],
                                    RAYON/2,
                                    N_POINTS)
pt_x = [x[0] for x in c2_points]
pt_y = [y[1] for y in c2_points]
scatter.set_offsets(np.hstack((pt_x[1*SPEED], pt_y[1*SPEED])))
fig.savefig('test_speed_twocircles_t0.png')
