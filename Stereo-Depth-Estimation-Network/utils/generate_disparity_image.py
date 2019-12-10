'''
Generate disparity image
'''
import skimage
import skimage.io
import inference


def generate_disparity_image(path_left, path_right):
    '''Store the disparity info into PNG image'''
    info = inference.main(path_left, path_right)
    img = (info*256).astype('uint16')
    new_path = path_left[:-4] + "_disparity.png"
    skimage.io.imsave(new_path, img)
