import sys
sys.path.append("..")
from utils import generate_depth_file
from utils import config
import pickle
import os
import numpy as np
import cv2


def test_generate_depth_file(path_left, path_right, baseline, focal, pixel_size):
    generate_depth_file.generate_depth_file(path_left, path_right, config.baseline, config.focal, config.pixel_size)
    new_path = path_left[:-4] + "_depth_info.pkl"
    if os.path.exists(new_path):
        file = open(new_path)
        file = pickle.load(file)
        img = cv2.imread(path_left)
        if np.shape(file) == np.shape(img[:,:,0]):
            print(np.shape(file))
        else:
            print("Wrong depth info generated")
    else:
        print("Failed to generate depth info file")

path_left = "../test/000047_10.png"
path_right = "../test/000047_10_r.png"
test_generate_depth_file(path_left, path_right, config.baseline, config.focal, config.pixel_size)
