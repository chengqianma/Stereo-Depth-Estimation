import sys
sys.path.append("..")
from utils import generate_disparity_image
import os
import cv2


def test_generate_disparity_image(path_left, path_right):
    generate_disparity_image.generate_disparity_image(path_left, path_right)
    new_path = path_left[:-4] + "_disparity.png"
    if os.path.exists(new_path):
        img = cv2.imread(new_path)
        cv2.imshow("Disparity image", img)
        cv2.waitKey(5000)
    else:
        print("Failed to generate disparity image")

path_left = "../test/000047_10.png"
path_right = "../test/000047_10_r.png"
test_generate_disparity_image(path_left, path_right)
