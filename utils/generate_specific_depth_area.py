import inference
import config
 
def generate_specific_depth_area(path_left, path_right, depth, config.baseline, config.focal, config.pixel_size):
    
    info = inference.main(path_left, path_right)
    disparity = (baseline * focal)/(depth * 2 * pixel_size)
    res = []
    for i in range(len(info)):
        for j in range(len(info[0])):
            if abs(img[i][j] - disparity) < 2:
                res.append([i,j])
    
    return res