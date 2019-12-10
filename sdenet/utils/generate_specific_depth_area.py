'''
Generate specific depth area
'''

import sys
sys.path.append("..")
from utils import inference
from utils import config


def generate_specific_depth_area(path_left, path_right, depth, baseline, focal, pixel_size):
    '''Store coordinates info of specific depth area'''
    info = inference.main(path_left, path_right)
    res = []
    max_depth = depth + config.RANGE
    min_depth = depth - config.RANGE
    min_disparity = (baseline * focal) / (max_depth * 2 * pixel_size)
    max_disparity = (baseline * focal) / (min_depth * 2 * pixel_size)
    for i in range(len(info)):
        for j in range(len(info[0])):
            if info[i][j] > min_disparity and info[i][j] < max_disparity:
                res.append([i, j])
    return res
