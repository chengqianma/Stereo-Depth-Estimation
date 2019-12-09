import inference
import skimage
import skimage.io


def generate_disparity_image(path_left, path_right):
    
    info = inference.main(path_left, path_right)
    img = (info*256).astype('uint16')
    new_path = path_left[:-4] + "_disparity.png"
    skimage.io.imsave(new_path, img)
