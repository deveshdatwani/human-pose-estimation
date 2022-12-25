# Human Body Pose Estimation

### Introduction

Human pose estimation is a computer vision technique to estimate and track human movement.
Highly-accurate real time human pose estimation is one of the biggest trends in computer vision in the
21st century. Research in this space has picked up after the advent of convolution based deep learning
methods. CNNs greatly reduce the learnable parameters for human pose estimation thus making it
computationally cheaper to estimate human pose in real time. Real time human pose estimations can have
many applications, some of them could be;
1. Athlete Performance Tracking
2. Human Health Evaluation
3. Augmented Reality Video Games
4. Agent motion prediction for autonomous driving
scDeep learning based classifiers and localisers are currently the most trending tool for object detection and tracking tasks. As a result of this, DNNs have seen rapid improvements in the last decade. Our project implements the model suggested by DeepPose which is an AlexNet with a regressor as the final layer as opposed to a classifier. DeepPose aims to take a holistic view of the human pose estimation problem and turn it into a joint regression problem.
There are two advantages to this approach. One, the network is capable of formulating the full context of the joint in each image; each joint uses the full image signal for regressing. This means that there is no need to separately model for each joint in the image frame. Second, the method is simpler compared to graphical models which need a human pose topology to predict interactions between body joints. In this report, we start by explaining the literature survey we carried out, our reasons for the chosen model for human pose estimation task, dataset selection and we finally then share our results.

<p align="center"><img src="https://raw.githubusercontent.com/deveshdatwani/human-pose-estimation/main/assets/CNNPOSE2.png"></p> 

### Model

We started with building an AlexNet from scratch with Tensorflow and Keras libraries. An AlexNet consists of 5 convolution layers which take an input of 227x227x3 dimensioned RGB image.
Each convolution layer is preceded by batch normalisation for faster convergence and therefore quicker
training. There are two pooling layers as shown in the image above. Each fully connected layer is
succeeded by a dropout layer. Our modification to this model was to replace the output layer with a 58
node fully connected layer to fit our dataset annotation style. The activation for this layer was changed to
linear from softmax as we’re regressing and not classifying anymore (which AlexNet was built for).

<p align="center"><img src="https://github.com/deveshdatwani/human-pose-estimation/blob/main/assets/CNNPose.png"></p> 

### Metric

So how can we evaluate our model accuracies? DeepPose suggests a metric for human pose estimation
called the PCP (percentage of correct parts).
The PCP metric says that if an estimated joint coordinate is no more than x units away from the ground
truth, the body joint is correctly detected. So how can we calculate “x”? X is calculated by thresholding
the torso diameter of the human in the image frame.
For example, let’s say an image has a human whose torso diameter is 50 units (50 pixels). Torso diameter
can be calculated by finding the euclidean distance between diagonally opposite shoulder and hip joints.
Figure 3 tries to schematically represent this.
Once this is done, we can threshold this distance by a factor. Let’s say we choose a factor of 0.3. This
would mean that if a joint is estimated in the 0.3 * (torso diameter) diameter, the joint would be classified
as correctly identified/detected. This would give us a boolean value for each joint estimation answering
the question; “was the joint localised correctly?”. This approach converts a regression task into a
classification task where accuracies / detection rates can be calculated. We’ve discussed our model
accuracy in the Model Evaluation section.
Intuitively, as we increase this threshold, the size of the diameter would become larger and consequently,
the detection rates would also go up. How we choose this threshold factor is entirely up to us, but
DeepPose suggests a maximum value of 0.3.

<p align="center"><img src="https://raw.githubusercontent.com/deveshdatwani/human-pose-estimation/main/assets/POS3.png"></p> 


### Method 

APPROACH:
There are two approaches for human pose estimation with machine learning.
1. Bottom-up: Estimate body joints in a given image frame and then build up the human pose.
2. Top down: To detect a human being in the image frame first and then build on the model to
estimate body joint locations.
In our project, we went for the bottom-up approach as proposed by the DeepPose paper, but also because
it’s a computationally cheaper task which fits our system capabilities and resources.
DATASET:
We trained our model on the FLIC dataset created by Sapp, Benjamin and Ben Taskar. It contains 5003
annotated images from Hollywood movies. The annotations of each image in this dataset contains
a. x,y coordinates of 29 joints of a human body
b. c: centre coordinates of the human in picture
c. image name
d. scale of the human in picture
MODEL:
We started with building an AlexNet from scratch with Tensorflow and Keras libraries.
An AlexNet consists of 5 convolution layers which take an input of 227x227x3 dimensioned RGB image.
Each convolution layer is preceded by batch normalisation for faster convergence and therefore quicker
training. There are two pooling layers as shown in the image above. Each fully connected layer is
succeeded by a dropout layer. Our modification to this model was to replace the output layer with a 58
node fully connected layer to fit our dataset annotation style. The activation for this layer was changed to
linear from softmax as we’re regressing and not classifying anymore (which AlexNet was built for).


### Training 

TRAINING PARAMETERS:
Epochs = 100
Batch Size = 32
Optimizer = Adam
Learning Rate = 0.0001
Loss = Mean Squared Error
Training Data Size = 4002 Images
Validation Data Size = 1001 Images
As mentioned in the methodology, the training was conducted on Google Collab with the help of GPU
acceleration service which brought training time by approximately 5 times.

<p align="center"><img src="https://raw.githubusercontent.com/deveshdatwani/human-pose-estimation/main/assets/THRESHOLD.png"></p> 

We observed the following results after the 100th epoch
Total training time ~ 5 hours
Mean squared error ~ 400
Root mean squared error ~ 20

### Model Evaluation

We decided to test our model on the validation set and push out images to observe the estimations. Some
of the results can be seen below in

It is important to note that the body joints that are not visible in the frame, were annotated as [-1,-1]. And
if the regressor estimated values close to that, the model plot scatter points at those joints.
From the above estimations, it can be observed that the model has learnt a human body shape and is good
at regressing it. However, estimations of some joints were still offset by quite a large margin.
The PCP metric is explained in the Metric section above. We selected 4 thresholds and calculated PCP for
each body joint for our 1001 validation dataset. The detection rate is represented by values on the y axis.
It is to be noted that our model performs poorly compared to the DeepPose model as DeepPose CNN has
been cascaded which is explained in section “Stage 2” later in this report.


<p align="center"><img src="https://raw.githubusercontent.com/deveshdatwani/human-pose-estimation/main/assets/SCREENTEST.png"></p> 

It was intuitive that the PCP metric increased as we increased the threshold factor.
Let’s further visualise what this means. Let’s take a look at the estimation in Figure 7. The right shoulder
estimate was offset by some value. We set a threshold of 0.2 of the torso diameter, we can draw a circle
on each joint with that value. If the joint estimation lies in that diameter, it means that the joint was
correctly estimated. In Figure 7, the right shoulder is not correctly estimated since the estimation lies
outside the threshold diameter

<p align="center"><img src="https://raw.githubusercontent.com/deveshdatwani/human-pose-estimation/main/assets/THRESHOLD.png"></p> 
<p align="center"><img src="https://raw.githubusercontent.com/deveshdatwani/human-pose-estimation/main/assets/POSETEST.png"></p> 

