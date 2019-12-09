import inference
import config


def generate_specific_depth_area(path_left, path_right, depth, baseline, focal, pixel_size):
    
    info = inference.main(path_left, path_right)
    res = []
    max_depth = depth + config.range
    min_depth = depth - config.range
    min_disparity = (baseline * focal) / (max_depth * 2 * pixel_size)
    max_disparity = (baseline * focal) / (min_depth * 2 * pixel_size)
    for i in range(len(info)):
        for j in range(len(info[0])):
            if info[i][j] > min_disparity and info[i][j] < max_disparity:
                res.append([i,j])
    
    return res