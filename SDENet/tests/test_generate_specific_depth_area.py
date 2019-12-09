import unittest
import numpy as np
import sys
sys.path.append("..")
from utils import display_depth
from utils import generate_specific_depth_area
from utils import config


path_left = "../sample_image/000047_10.png"
path_right = "../sample_image/000047_10_r.png"
path_result = "../sample_image/000047_10_disparity.png"

max_depth, min_depth = display_depth.max_min_depth(path_result, config.baseline, config.focal, config.pixel_size)


class TestCase(unittest.TestCase):

    def test_depth_upper_bound(self):
        depth = max_depth
        area = generate_specific_depth_area.generate_specific_depth_area(path_left, path_right, depth, config.baseline,
                                                                         config.focal, config.pixel_size)
        self.assertIsNot(area, [], "Generated error")

    def test_depth_lower_bound(self):
        depth = min_depth
        area = generate_specific_depth_area.generate_specific_depth_area(path_left, path_right, depth,
                                                                         config.baseline, config.focal, config.pixel_size)
        self.assertIsNot(area, [], "Generated error")

    def test_depth_out_of_range(self):
        depth = max_depth + min_depth
        area = generate_specific_depth_area.generate_specific_depth_area(path_left, path_right, depth,
                                                                         config.baseline, config.focal, config.pixel_size)
        self.assertEqual(area, [], "Generated error")

    def test_depth_format(self):
        depth = min_depth
        area = generate_specific_depth_area.generate_specific_depth_area(path_left, path_right, depth, config.baseline, config.focal,
                                                                         config.pixel_size)
        self.assertEqual(np.shape(area)[1], 2, "Generated error")


if __name__ == '__main__':
    unittest.main()