import Test_img
import pickle


def generate_depth_file(path_left, path_right, baseline, focal, pixel_size):
    info = Test_img.main(path_left, path_right)
    for i in range(len(info)):
        for j in range(len(info[0])):
            info[i][j] = (baseline * focal) / (info[i][j] * 2 * pixel_size)
    file = open("depth_info.pkl", "wb") 
    pickle.dump(info, file)

