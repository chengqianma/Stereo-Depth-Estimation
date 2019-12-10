'''
Generate depth pickle file 
'''
import sys
sys.path.append("..")
import pickle
from utils import inference


def generate_depth_file(path_left, path_right, baseline, focal, pixel_size):
    '''Store the depth output into pickle file'''
    info = inference.main(path_left, path_right)
    for i in range(len(info)):
        for j in range(len(info[0])):
            info[i][j] = (baseline * focal) / (info[i][j] * 2 * pixel_size)
    new_path = path_left[:-4] + "_depth_info.pkl"
    file = open(new_path, "wb")
    pickle.dump(info, file)
