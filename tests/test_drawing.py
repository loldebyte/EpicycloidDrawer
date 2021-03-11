from matplotlib.testing.decorators import image_comparison
import epicycloid_drawer.core


def test_one_circle_basic():
    @image_comparison(baseline_images=['test_1circle'],
                      extensions=['png'])
    def test_basic_circle():
        epicycloid_drawer.core.draw_image(r=[.5])

    @image_comparison(baseline_images=['test_1circle_t1'],
                      extensions=['png'])
    def test_basic_circle_t1():
        epicycloid_drawer.core.draw_image(r=[.5], t=1)


def test_one_circle_radius():
    @image_comparison(baseline_images=['test_radius_1circle'],
                      extensions=['png'])
    def test_diameter():
        epicycloid_drawer.core.draw_image(r=[1])

    @image_comparison(baseline_images=['test_radius_1circle_t1'],
                      extensions=['png'])
    def test_diameter_t1():
        epicycloid_drawer.core.draw_image(r=[1], t=1)


def test_one_circle_speed():
    @image_comparison(baseline_images=['test_speed_1circle'],
                      extensions=['png'])
    def test_speed():
        epicycloid_drawer.core.draw_image(r=[.5], s=10)

    @image_comparison(baseline_images=['test_speed_1circle_t1'],
                      extensions=['png'])
    def test_speed_t1():
        epicycloid_drawer.core.draw_image(r=[.5], s=10, t=1)


def test_one_circle_phase():
    # TODO: add @image_comparisons to all test functions
    def test_phase():
        epicycloid_drawer.core.draw_image(r=[.5], theta=[30])

    def test_phase_t1():
        epicycloid_drawer.core.draw_image(r=[.5], theta=[30], t=1)


def test_one_circle_all():
    def test_all():
        epicycloid_drawer.core.draw_image(r=[1], s=10, theta=[30])

    def test_all_t1():
        epicycloid_drawer.core.draw_image(r=[1], s=10, theta=[30], t=1)
