# Component Specification
## Software Components

#### GUI:
- What it does: Allow users to input stereo images or stereo videos through graphic user interface and give the data to the backend. At last, get the depth image or video from the backend and display it.
- Input: Stereo images or Videos
- Output: Depth image or Video

#### Data Processing :
- What it does: Get the input images or videos from the GUI. Change the image into the suitable datatype. Or split the video into images. And finally turned them into tensor from.
- Input : Stereo images or Videos
- Output : Tensor form

#### Model :
- What it does : Construct the network structure using torch packages, compute and analyse the depth information in each image.
- Input it requires: Tensor transformed from images
- Output it requires: Tensor results

#### Training :
- What it does : Train the model and fintune the parameters with different datasets by torch package.
- Input: Tensor from data processing
- Output: Loss and accuracy during the trainning process

#### Prediction :
- What it does : Load the trained model weights and transfer the depth images from the tensor results.
- Input: Model weights & Tensor results
- Output: Estimated depth images tagged with colors 



## Interactions to Accomplish Use Cases
As for the autonomous driving case, the system will estimate the distance between all things in images like pedestrian, vehicles, obstacles, etc. and our own car. The input will be just a real-time image captured by stereo cameras on cars. The output is a depth image that lighter color means the part in image is much more closer to our car. Before this prediction process, the system needs plenty of images and tagged depth information to train the model, adjusting the parameters.


## Plan and Schedule
- Data Processing -- Finished
Converting video to images if any. Adjusting features of images as input, like brightness and contrast. Fuzzing processing applies. Converting the input into tensor form that the model can take in. Re-adjusting the quality of pictures according to the feedback of the training and testing model.
- Model Construction -- Finished
Based on existing models, constructing and improving the Network Structure.
- Hyperparameters Setup & Model Training
- Depth Estimation & Visualization
Obtaining the tensor of the depth of input images or videos. Evaluating the results of training and testing process. Constructing Graphical User Interface. 


