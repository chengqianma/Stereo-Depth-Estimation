'''
Dispaly specific depth area
'''
import numpy as np
import cv2
import config


def display_depth(path, depth):
    '''Given depth and show the corresponding area in white'''
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    max_depth = depth + config.RANGE
    min_depth = depth - config.RANGE
    min_disparity = (config.BASELINE * config.FOCAL)/(max_depth * 2 * config.PIXEL_SIZE)
    max_disparity = (config.BASELINE * config.FOCAL) / (min_depth * 2 * config.PIXEL_SIZE)
    for i in range(len(img)):
        for j in range(len(img[0])):
            if img[i][j] > min_disparity and img[i][j] < max_disparity:
                img[i][j] = 255

    cv2.imwrite("depth_temp.png", img)

def max_min_depth(path, baseline, focal, pixel_size):
    '''Find the minimum and maximum depth in a given image'''
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    temp_dis_min = max(map(max, img))
    temp_dis_max = min(map(min, img))
    max_dis = (baseline * focal) / (temp_dis_max * 2 * pixel_size)
    max_dis = int(np.floor(max_dis))
    min_dis = (baseline * focal) / (temp_dis_min * 2 * pixel_size)
    min_dis = int(np.ceil((min_dis)))

    return max_dis, min_dis
    