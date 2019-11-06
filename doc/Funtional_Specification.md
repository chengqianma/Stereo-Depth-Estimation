## Functional Specification
--------------------
###Background
Depth estimation from stereo cameras has been a research topic for a long time.Since depth estimation from stereo images is essential to computer vision applications, including autonomous driving for vehicles, 3D model reconstruction, and object detection and recognition. 

Traditional method uses disparity between stereo camera images to cacluate the depth, but it still has lots of problems in cacluating the disparity map especially in potential feature matching part. 

With the fast development of deep learning, people can do a much better job in feature matching by using convolutional nerual network. So we want to use deep learning method to do the depth estimation from stereo cameras.

### User profile

Professional engineers such as autonomous driving researchers, AR developers, and developers of image-processing software. They may not use python but must be skilled in calling software packages and extracting information from images. They should harbor solid understanding of numerical methods, optimization, structure from motion, signal and image processing, probabilistic methods.

### Data sources
- KITTI 2015: a real-world dataset with street views from a driving car. It contains 200 training stereo image pairs with sparse ground-truth disparities obtained using LiDAR and another 200 testing image pairs without ground-truth disparities. Image size is H = 376 and W = 1240.
http://www.cvlibs.net/datasets/kitti/

- Scene Flow: a large scale synthetic dataset containing 35454 training and 4370 testing images with H = 540 and W = 960. This dataset provides dense and elaborate disparity maps as ground truth.
https://lmb.informatik.uni-freiburg.de/resources/datasets/SceneFlowDatasets.en.html

### Use cases
--------------------------------
#### Use case 1 
##### Autonomous driving
Autonomous developers will provide or input some kind of real-time images catched by the stereo cameras on car, which capture the vehicle or environment situations around the car.  After the computation and analysis, our system will come out with some kind of depth images to tell the developers the real distance between the actual items in images and the stereo cameras(or the car). It is essential for the autonomous system to do the judgement and make further actions.

#### Use case 2
##### AI photography
AI developers for photography will provide images captured by smartphones. After the extraction and analysis, our system will come out with the depth images indicate that the distance between the shooting objects and background, which could be used to applying DOF(depth of field) effects for those non-professional photograph devices.

#### Use case 3
##### AR
AR developers for applications like measurements, education, gaming, etc. will provide a series of images or videos. After the analysis and prediction, out system will come out with the depth information for developers to estimate the positions of some items in 3-dimension space and construct models.
