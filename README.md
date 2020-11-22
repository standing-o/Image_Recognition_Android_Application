# Image Recognition Android Application (20200706 ~)
- A mobile android application that uses Deeplearning to recognize images in real-time taken by the mobile phone's camera.
- This project is maintained by [정명지](https://github.com/mongdii), 오서영, [강성원](https://github.com/Soric-stu)
- Our Team name is **"Trinity"**  

## Process
#### 1. 20200706 ~ 20200712  

|Developer|Individual Role|-|
|---|------|------|
|정명지|Basic bio study, image crawling|
|오서영|Basic Machine learning presentation - Overview | [[Presentation]](https://github.com/OH-Seoyoung/Image_Recognition_Android_Application/blob/master/Presentation/20200710_basic_ML_1.pdf)|
|강성원|Basic JAVA presentation - Overview|  

#### 2. 20200713 ~ 20200719  

|Developer|Individual Role|-|
|---|------|------|
|정명지|Handwriting application structure design | [[Rough design]](https://github.com/OH-Seoyoung/Image_Recognition_Android_Application/tree/master/Rough_Design)|
|오서영|Basic ML presentation - **Image classification with CNN** | [[Presentation]](https://github.com/OH-Seoyoung/Image_Recognition_Android_Application/blob/master/Presentation/20200710_basic_ML_2.pdf)|
|강성원|Basic JAVA presentation - **Android Studio**|  

#### 3. 20200727 ~ 20200803  

|Developer|Individual Role|-|
|---|------|------|
|정명지|Data collection - flower dataset (image)|
|오서영|Mobile app design - icon, color, view | [[Main screen design]](https://github.com/OH-Seoyoung/Image_Recognition_Android_Application/tree/master/Main_Design/main_screen)|
|강성원|Mobile app - touch slide motion event|  

#### 4. 20200803 ~ 20200809  

|Developer|Individual Role|-|
|---|------|------|
|정명지|Data collection - flower dataset (common/scientific name) | [[In-app dataset]](https://github.com/OH-Seoyoung/Image_Recognition_Android_Application/tree/master/In-app_Data)|
|오서영|Banner design, **Baseline CNN** with flower image dataset | [[Banner design]](https://github.com/OH-Seoyoung/Image_Recognition_Android_Application/tree/master/Main_Design/launch_screen)  [[Code]](https://github.com/OH-Seoyoung/Image_Recognition_Android_Application/blob/master/Image_recognition_DeepLearning_Models/20200807_baseline_CNN/Baseline_CNN.ipynb)|
|강성원|Mobile app - UI relocation, touch event|  

#### 5. 20200810 ~ 20200816  

|Developer|Individual Role|-|
|---|------|------|
|정명지|Google Image crawling for training|
|오서영|Single layer NN Presentation for study, **Resnet** | [[Presentation]](https://github.com/OH-Seoyoung/Image_Recognition_Android_Application/blob/master/Presentation_for_study/20200816_basic_ML_3/20200816_Single_Layer_Neural_Network.ipynb) | [[Code]](https://github.com/OH-Seoyoung/Image_Recognition_Android_Application/blob/master/Image_recognition_DeepLearning_Models/20200816_Resnet_code/Resnet_with_flower_dataset.ipynb)|
|강성원|Android Studio Presentation for study, Mobile app - Animation, in-app data insertion|  

#### 6. 20200817 ~ 20200823  

|Developer|Individual Role|-|
|---|------|------|
|정명지|Google Image crawling for training|
|오서영|Model Selection to complement accuracy, Page Design | [[Code]](https://github.com/OH-Seoyoung/Image_Recognition_Android_Application/tree/master/Image_recognition_DeepLearning_Models/20200823_Model_Selection_with_more_data) | [[Design]](https://github.com/OH-Seoyoung/Image_Recognition_Android_Application/tree/master/Main_Design)|
|강성원|Mobile app - Add new pages with page design|  

#### 7. 20200824 ~ 20200830  

|Developer|Individual Role|-|
|---|------|------|
|정명지|Study AI and JAVA for report|
|오서영|Test with a sample | [[Test]](https://github.com/OH-Seoyoung/Image_Recognition_Android_Application/blob/master/Image_recognition_DeepLearning_Models/20200830_Model_Selection_Final/Test.ipynb)|
|강성원|Mobile app - Implement camera, build data models|  

#### 8. 20200831 ~  

|Developer|Individual Role|-|
|---|------|------|
|정명지|Write up report|
|오서영|Connecting Tensorflow Models to Android Studio, Icon Design | [[Code]](https://github.com/OH-Seoyoung/Image_Recognition_Android_Application/tree/master/Image_recognition_DeepLearning_Models/20200906_Connect_to_Android) | [[Icon]](https://github.com/OH-Seoyoung/Image_Recognition_Android_Application/tree/master/Main_Design/menu_icon)|
|강성원|Connecting Tensorflow Models to Android Studio|  

> Applying Tensorflow to Android
1. Convert h5 to pb
2. Convert pb to tflite  
3. Make test.py file | [[Code]](https://github.com/OH-Seoyoung/Image_Recognition_Android_Application/tree/master/Image_recognition_DeepLearning_Models/20201119_Test_in_Android)  

## Dataset for DeepLearning
- Tensorflow Flower Dataset : **5** classes (daisy, dandelion, roses, sunflowers, tulips)
```
[1] tf_flowers, https://www.tensorflow.org/datasets/catalog/tf_flowers
```

## Results  
### 2939 training set with 5 class
#### 1. Baseline **CNN** (100 iterations, 32 batch) | [[Code]](https://github.com/OH-Seoyoung/Image_Recognition_Android_Application/tree/master/Image_recognition_DeepLearning_Models/20200807_baseline_CNN_code)  
Train accuracy: 85.62%  
Val accuracy: 69.38%

#### 2. **Resnet** (50 iterations, 32 batch) | [[Code]](https://github.com/OH-Seoyoung/Image_Recognition_Android_Application/tree/master/Image_recognition_DeepLearning_Models/20200816_Resnet_code)  
Train accuracy : 85.00%  
Val accuracy : 66.25%

### 4685 training set with 5 class | [[Code]](https://github.com/OH-Seoyoung/Image_Recognition_Android_Application/tree/master/Image_recognition_DeepLearning_Models/20200823_Model_Selection_with_more_data)  
#### 1. Baseline **CNN** (100 iterations, 64 batch)  
Train accuracy: 72.19%  
Val accuracy: 70.00%  

#### 2. Baseline **CNN** (100 iterations, 32 batch)  
Train accuracy: 83.13%  
Val accuracy: 73.12%  

#### 3. Baseline **CNN** (100 iterations, 16 batch)  
Train accuracy: 95.00%  
Val accuracy: 73.75%  

#### 4. **Resnet** (50 iterations, 32 batch)  
Train accuracy: 79.37%  
Val accuracy: 65.62%  

#### 5. Baseline **CNN** (100 iterations, no batch)  
Train accuracy: 80.00%  
Val accuracy: 80.00%

## Reference
```
[1] Advanced Computer Vision with TensorFlow, https://stephan-osterburg.gitbook.io/coding/coding/ml-dl/tensorfow    
```




