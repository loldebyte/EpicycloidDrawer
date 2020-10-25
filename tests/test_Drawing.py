import unittest
from matplotlib.testing.decorators import image_comparison
import EpicycloidDrawer.core


class TestOneCircleBasic(unittest.TestCase):
    @image_comparison(baseline_images=['test_1circle'],
                      extensions=['png'])
    def test_basic_circle(self):
        EpicycloidDrawer.core.draw_image(r=[.5])

    @image_comparison(baseline_images=['test_1circle_t1'],
                      extensions=['png'])
    def test_basic_circle_t1(self):
        EpicycloidDrawer.core.draw_image(r=[.5], t=1)


class TestOneCircleRadius(unittest.TestCase):
    @image_comparison(baseline_images=['test_radius_1circle'],
                      extensions=['png'])
    def test_diameter(self):
        EpicycloidDrawer.core.draw_image(r=[1])

    @image_comparison(baseline_images=['test_radius_1circle_t1'],
                      extensions=['png'])
    def test_diameter_t1(self):
        EpicycloidDrawer.core.draw_image(r=[1], t=1)


class TestOneCircleSpeed(unittest.TestCase):
    # TODO: add @image_comparisons to all test functions
    def test_speed(self):
        EpicycloidDrawer.core.draw_image(r=[.5], s=10)

    def test_speed_t1(self):
        EpicycloidDrawer.core.draw_image(r=[.5], s=10, t=1)


class TestOneCirclePhase(unittest.TestCase):
    def test_phase(self):
        EpicycloidDrawer.core.draw_image(r=[.5], theta=[30])

    def test_phase_t1(self):
        EpicycloidDrawer.core.draw_image(r=[.5], theta=[30], t=1)


class TestOneCircleAll(unittest.TestCase):
    def test_all(self):
        EpicycloidDrawer.core.draw_image(r=[1], s=10, theta=[30])

    def test_all_t1(self):
        EpicycloidDrawer.core.draw_image(r=[1], s=10, theta=[30], t=1)


if __name__ == '__main__':
    unittest.main()
