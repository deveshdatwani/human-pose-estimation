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

### Model

We started with building an AlexNet from scratch with Tensorflow and Keras libraries. An AlexNet consists of 5 convolution layers which take an input of 227x227x3 dimensioned RGB image.
Each convolution layer is preceded by batch normalisation for faster convergence and therefore quicker
training. There are two pooling layers as shown in the image above. Each fully connected layer is
succeeded by a dropout layer. Our modification to this model was to replace the output layer with a 58
node fully connected layer to fit our dataset annotation style. The activation for this layer was changed to
linear from softmax as we’re regressing and not classifying anymore (which AlexNet was built for).
