'''
Test the function of the generation of depth file
'''
import os
import unittest
import sys
sys.path.append("..")
from utils import generate_depth_file
import config


class TestCase(unittest.TestCase):
    '''Test case'''
    def test_generate_depth_file(self):
        '''Test if the function generate the depth file'''
        generate_depth_file.generate_depth_file(config.PATH_LEFT, config.PATH_RIGHT,
                                                config.BASELINE, config.FOCAL, config.PIXEL_SIZE)
        new_path = config.PATH_LEFT[:-4] + "_depth_info.pkl"
        is_exist = os.path.exists(new_path)
        self.assertTrue(is_exist)


if __name__ == '__main__':
    unittest.main()
    