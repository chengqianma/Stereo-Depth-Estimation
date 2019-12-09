import sys
sys.path.append("..")
from utils import generate_depth_file
from utils import config
import os
import unittest

path_left = "../test/000047_10.png"
path_right = "../test/000047_10_r.png"


class TestCase(unittest.TestCase):

    def test_generate_depth_file(self):
        generate_depth_file.generate_depth_file(path_left, path_right, config.baseline, config.focal, config.pixel_size)
        new_path = path_left[:-4] + "_depth_info.pkl"
        is_exist = os.path.exists(new_path)
        self.assertTrue(is_exist)




if __name__ == '__main__':
    unittest.main()