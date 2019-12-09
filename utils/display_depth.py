import cv2
import numpy as np
import config
"""
path = "D:/Picture/User.jpg"
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray)
"""

def display_depth(path, depth):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h = len(img)
    w = len(img[0])
    max_depth = depth + config.range
    min_depth = depth - config.range
    min_disparity = (config.baseline * config.focal)/(max_depth * 2 * config.pixel_size)
    max_disparity = (config.baseline * config.focal) / (min_depth * 2 * config.pixel_size)
    for i in range(h):
        for j in range(w):
            if img[i][j] > min_disparity and img[i][j] < max_disparity:
                img[i][j] = 255

    cv2.imwrite("depth_temp.png", img)

def max_min_depth(path, baseline, focal, pixel_size):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    temp_dis_min = max(map(max, img))
    temp_dis_max = min(map(min, img))
    max_dis = (baseline * focal) / (temp_dis_max * 2 * pixel_size)
    max_dis = int(np.floor(max_dis))
    min_dis = (baseline * focal) / (temp_dis_min * 2 * pixel_size)
    min_dis = int(np.ceil((min_dis)))

    return max_dis, min_dis
    
