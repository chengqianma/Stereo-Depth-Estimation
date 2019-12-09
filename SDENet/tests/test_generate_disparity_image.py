import sys
sys.path.append("..")
from utils import generate_disparity_image
import os
import cv2
import numpy as np
import unittest


path_left = "../sample_image/000047_10.png"
path_right = "../sample_image/000047_10_r.png"


class TestCase(unittest.TestCase):

    def test_generate_disparity_image(self):
        generate_disparity_image.generate_disparity_image(path_left, path_right)
        new_path = path_left[:-4] + "_disparity.png"
        is_exist = os.path.exists(new_path)
        self.assertTrue(is_exist)

    def test_disparity_size(self):
        generate_disparity_image.generate_disparity_image(path_left, path_right)
        new_path = path_left[:-4] + "_disparity.png"
        input_img = cv2.imread(path_left)
        output_img = cv2.imread(new_path)
        self.assertEqual(np.shape(input_img), np.shape(output_img), "Disparity size error")


if __name__ == '__main__':
    unittest.main()