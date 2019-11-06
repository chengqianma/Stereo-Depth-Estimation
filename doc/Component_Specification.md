# Component Specification
##Software components
#### Data processing : 
- What it does: Use OpenCV package to read the image from the dataset. Use the torch package to split the data into batches and normalize it. 
- Input: Images in datasets
- Output: Tensor 

#### Model :
- What it does : Compute and analyse the depth information by torch package
- Input: Tensor from data processing
- Output: Tensor 

####Training :
- What it does : Train and finetune the model with different datasets by torch package
- Input: Tensor from data processing
- Output: Loss and accuracy during the trainning process

#### Predict :
- What it does : Predict the depth information from the stereo images and convert the depth information into a image.
- Input: Stereo images
- Output: estimated depth image 