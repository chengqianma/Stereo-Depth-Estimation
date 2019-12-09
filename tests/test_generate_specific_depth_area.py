import sys
sys.path.append("..")
from utils import display_depth
from utils import generate_specific_depth_area
from utils import config


def test_generate_specific_depth_area(path_left, path_right, depth, baseline, focal, pixel_size):
    area = generate_specific_depth_area.generate_specific_depth_area(path_left, path_right, depth, config.baseline, config.focal, config.pixel_size)
    max_depth, min_depth = display_depth.max_min_depth(path_result, config.baseline, config.focal, config.pixel_size)
    if depth < min_depth - config.range or depth > max_depth + config.range:
        if area:
            print("Wrong area generated")
        else:
            print("Input depth out of range")
    else:
        if not area:
            print("Failed to generated specific depth area")
        else:
            for i in range(len(area)):
                for j in range(len(area[i])):
                    if j > 1:
                        print("Wrong coordinate generated")
                        return
                    if type(area[i][j]) is not type(area[0][0]):
                        print("Wrong data type")
                        return
        print("Specific depth area generated")

path_left = "../test/000047_10.png"
path_right = "../test/000047_10_r.png"
path_result = "../test/000047_10_disparity.png"
for i in range(90, 100, 20):
    depth = i
    test_generate_specific_depth_area(path_left, path_right, depth, config.baseline, config.focal, config.pixel_size)
