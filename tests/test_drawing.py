import pytest
import epicycloid_drawer


def test_one_circle_basic():
    @pytest.mark.mpl_image_compare(baseline_dir='baseline_images',
                                   filename='1circle.png')
    def test_basic_circle():
        epicycloid_drawer.draw_circle()

    @pytest.mark.mpl_image_compare(baseline_dir='baseline_images',
                                   filename='1circle_t1.png')
    def test_basic_circle_t1():
        epicycloid_drawer.draw_circle(t=1)


def test_one_circle_radius():
    @pytest.mark.mpl_image_compare(baseline_dir='baseline_images',
                                   filename='test_radius_1circle_t0.png')
    def test_diameter():
        epicycloid_drawer.core.draw_image(r=[1])

    @pytest.mark.mpl_image_compare(baseline_dir='baseline_images',
                                   filename='test_radius_1circle_t1.png')
    def test_diameter_t1():
        epicycloid_drawer.core.draw_image(r=[1], t=1)


def test_one_circle_speed():
    @pytest.mark.mpl_image_compare(baseline_dir='baseline_images',
                                   filename='test_speed_1circle_t0.png')
    def test_speed():
        epicycloid_drawer.core.draw_image(r=[.5], s=10)

    @pytest.mark.mpl_image_compare(baseline_dir='baseline_images',
                                   filename='test_speed_1circle_t1.png')
    def test_speed_t1():
        epicycloid_drawer.core.draw_image(r=[.5], s=10, t=1)


def test_one_circle_phase():
    @pytest.mark.mpl_image_compare(baseline_dir='baseline_images',
                                   filename='test_phase_1circle_t0.png')
    def test_phase():
        epicycloid_drawer.core.draw_image(r=[.5], theta=[30])

    @pytest.mark.mpl_image_compare(baseline_dir='baseline_images',
                                   filename='test_phase_1circle_t1.png')
    def test_phase_t1():
        epicycloid_drawer.core.draw_image(r=[.5], theta=[30], t=1)


def test_one_circle_all():
    @pytest.mark.mpl_image_compare(baseline_dir='baseline_images',
                                   filename='test_all_1circle_t0.png')
    def test_all():
        epicycloid_drawer.core.draw_image(r=[1], s=10, theta=[30])

    @pytest.mark.mpl_image_compare(baseline_dir='baseline_images',
                                   filename='test_all_1circle_t1.png')
    def test_all_t1():
        epicycloid_drawer.core.draw_image(r=[1], s=10, theta=[30], t=1)
