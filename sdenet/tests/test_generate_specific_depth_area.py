'''
Test the function of the generation of specific depth area
'''
import unittest
import sys
import numpy as np
sys.path.append("..")
from utils import display_depth
from utils import generate_specific_depth_area
import config


MAX_DEPTH, MIN_DEPTH = display_depth.max_min_depth(config.PATH_RESULT,
                                                   config.BASELINE, config.FOCAL, config.PIXEL_SIZE)


class TestCase(unittest.TestCase):
    '''Test cases'''
    def test_depth_upper_bound(self):
        '''Test if the maximum depth could match some area'''
        depth = MAX_DEPTH
        area = generate_specific_depth_area.generate_specific_depth_area(config.PATH_LEFT,
                                                                         config.PATH_RIGHT,
                                                                         depth, config.BASELINE,
                                                                         config.FOCAL,
                                                                         config.PIXEL_SIZE)
        self.assertIsNot(area, [], "Generated error")

    def test_depth_lower_bound(self):
        '''Test if the minimum depth could match some area'''
        depth = MIN_DEPTH
        area = generate_specific_depth_area.generate_specific_depth_area(config.PATH_LEFT,
                                                                         config.PATH_RIGHT,
                                                                         depth, config.BASELINE,
                                                                         config.FOCAL,
                                                                         config.PIXEL_SIZE)
        self.assertIsNot(area, [], "Generated error")

    def test_depth_out_of_range(self):
        '''Test if error input could cause error generation'''
        depth = MAX_DEPTH + MIN_DEPTH
        area = generate_specific_depth_area.generate_specific_depth_area(config.PATH_LEFT,
                                                                         config.PATH_RIGHT,
                                                                         depth, config.BASELINE,
                                                                         config.FOCAL,
                                                                         config.PIXEL_SIZE)
        self.assertEqual(area, [], "Generated error")

    def test_depth_format(self):
        '''Test the output area data format'''
        depth = MIN_DEPTH
        area = generate_specific_depth_area.generate_specific_depth_area(config.PATH_LEFT,
                                                                         config.PATH_RIGHT,
                                                                         depth, config.BASELINE,
                                                                         config.FOCAL,
                                                                         config.PIXEL_SIZE)
        self.assertEqual(np.shape(area)[1], 2, "Generated error")


if __name__ == '__main__':
    unittest.main()
  