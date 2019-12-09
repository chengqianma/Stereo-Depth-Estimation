# Stereo-Depth-Estimation-Network
----------------------------------
**Contributors**
- Chengqian Ma
- Bingkun Li
- Robert Chang

## Background
Depth estimation from stereo cameras has been a research topic for a long time. Since depth estimation from stereo images is essential to computer vision applications, including autonomous driving for vehicles, 3D model reconstruction, and object detection and recognition.

Traditional method uses disparity between stereo camera images to calculate the depth, but it has problems in calculating the disparity map especially in the matching part of potential features.

With the fast development of deep learning, people can do a better job in feature matching by using Convolutional Neural Network. We want to use deep-learning method to achieve the depth estimation based on stereo cameras.

## Organization of the project

The package is organized as the following structure:

    Stereo-Depth-Estimation-Network(master)
    /--- doc/
        /--- Component_Specification.md
        /--- Functional_Specification.md
    /--- models/
        /--- basic.py
        /--- stackhourglass.py
        /--- submodule.py
        /--- trained/
        /--- KITTI2015.tar
        /--- sceneflow.tar
    /--- utils/
        /--- inference.py
        /--- displayDepth.py
        /--- preprocess.py
        /--- readpfm.py
    /--- README.md
    /--- LICENSE
    /--- GUI.py
    
## Data sources
- KITTI 2015: a real-world dataset with street views from a driving car. It contains 200 training stereo image pairs with sparse ground-truth disparities obtained using LiDAR and another 200 testing image pairs without ground-truth disparities. Image size is H = 376 and W = 1240.
http://www.cvlibs.net/datasets/kitti/

- Scene Flow: a large scale synthetic dataset containing 35454 training and 4370 testing images with H = 540 and W = 960. This dataset provides dense and elaborate disparity maps as ground truth.
https://lmb.informatik.uni-freiburg.de/resources/datasets/SceneFlowDatasets.en.html

## Installation
#### Step 1: Install Stereo-Depth-Estimation-Network by cloning it on you computer with `git` command:

```
git clone https://github.com/chengqianma/Stereo-Depth-Estimation-Network.git
```

#### Step 2: Install the the package you need in the environment by running `setup.py`  file:

```
cd Stereo-Depth-Estimation-Network/
python setup.py install
```

#### Step 3: Check the dependencies to run `Stereo-Depth-Estimation-Network` are completely installed on your computer by running the command:

```
pip install -r requirements.txt
```

Now, you should be ready to run `Stereo-Depth-Estimation-Network` on  your computer. 

## Tutorial: how to use
Make sure that the camera parameters in `config.py` are correctly corresponding to the dataset you want to use. Default settings are based on KITTI 2015.

users modify camera parameters. config.py

api generate_depth, takes in left image and right image.  depth info matrix with unit: m in `.pickle` file

api generate_disparity_image takes in left image and right image. returns `.png` file. 

api generate_specific_depth_area: take in left path, right path and depth can be float. returns a list[x, y]