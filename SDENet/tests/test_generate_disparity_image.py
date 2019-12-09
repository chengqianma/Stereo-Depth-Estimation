'''
Test the function of the generation of disparity image
'''
import os
import unittest
import sys
import numpy as np
import cv2
sys.path.append("..")
from utils import generate_disparity_image
from utils import config


class TestCase(unittest.TestCase):
    '''Test cases'''
    def test_generate_disparity_image(self):
        '''Test if generate the disparity image'''
        generate_disparity_image.generate_disparity_image(config.PATH_LEFT, config.PATH_RIGHT)
        new_path = config.PATH_LEFT[:-4] + "_disparity.png"
        is_exist = os.path.exists(new_path)
        self.assertTrue(is_exist)

    def test_disparity_size(self):
        '''Test if the disparity size is correct'''
        generate_disparity_image.generate_disparity_image(config.PATH_LEFT, config.PATH_RIGHT)
        new_path = config.PATH_LEFT[:-4] + "_disparity.png"
        input_img = cv2.imread(config.PATH_LEFT)
        output_img = cv2.imread(new_path)
        self.assertEqual(np.shape(input_img), np.shape(output_img), "Disparity size error")


if __name__ == '__main__':
    unittest.main()
    