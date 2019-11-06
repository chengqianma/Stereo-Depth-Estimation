# Component Specification
## Software Components
#### Data Processing : 
- What it does: Use OpenCV package to open and store images from the dataset. Split the data into small batches for later training and normalize them with torch package. 
- Input it requires: Images in datasets
- Output it requires: Tensor form

#### Model :
- What it does : Construct the network structure using torch packages, compute and analyse the depth information in each image.
- Input it requires: Tensor transformed from images
- Output it requires: Tensor results

#### Training :
- What it does : Train the model and fintune the parameters with different datasets by torch package.
- Input: Tensor from data processing
- Output: Loss and accuracy during the trainning process

#### Prediction :
- What it does : Predict the depth information from the stereo images and convert it into images.
- Input: Stereo Images
- Output: Estimated depth images tagged with colors 

## Interactions to Accomplish Use Cases
As for the autonomous driving case, the system will estimate the distance between all things in images like pedestrian, vehicles, obstacles, etc. and our own car. The input will be just a real-time image captured by stereo cameras on cars. The output is a depth image that lighter color means the part in image is much more closer to our car. Before this prediction process, the system needs plenty of images and tagged depth information to train the model, adjusting the parameters.

## Preliminary Plan
- Data Processing
- Model Construction
- Hyperparameters Setup & Model Training
- Depth Estimation & Visualization

We have already finished the first two steps, we will focus on the rest parts in the coming weeks.