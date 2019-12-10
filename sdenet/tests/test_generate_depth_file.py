'''
Test the function of the generation of depth file
'''
import os
import unittest
import sys
sys.path.append("..")
from utils import generate_depth_file
import config
import pickle
import cv2
import numpy as np

class TestCase(unittest.TestCase):
    '''Test case'''
    def test_generate_depth_file(self):
        '''Test if the function generate the depth file'''
        generate_depth_file.generate_depth_file(config.PATH_LEFT, config.PATH_RIGHT,
                                                config.BASELINE, config.FOCAL, config.PIXEL_SIZE)
        new_path = config.PATH_LEFT[:-4] + "_depth_info.pkl"
        is_exist = os.path.exists(new_path)
        self.assertTrue(is_exist)

    def test_pickle_file(self):
        '''Test whether the depth file is empty or not'''
        generate_depth_file.generate_depth_file(config.PATH_LEFT, config.PATH_RIGHT,
                                                config.BASELINE, config.FOCAL, config.PIXEL_SIZE)
        new_path = config.PATH_LEFT[:-4] + "_depth_info.pkl"
        file = open(new_path)
        file = pickle.load(file)
        self.assertIsNot(file, [], "Generate wrong depth file")

    def test_depth_info(self):
        '''Test the matrix size of the depth file'''
        generate_depth_file.generate_depth_file(config.PATH_LEFT, config.PATH_RIGHT,
                                                config.BASELINE, config.FOCAL, config.PIXEL_SIZE)
        new_path = config.PATH_LEFT[:-4] + "_depth_info.pkl"
        file = open(new_path)
        matrix = pickle.load(file)
        img = cv2.imread(config.PATH_LEFT)
        self.assertEqual(np.shape(matrix), np.shape(img[:,:,0]), "Disparity size error")

if __name__ == '__main__':
    unittest.main()
    