#!/usr/bin/env python
# coding: utf-8

import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image
from keras.models import model_from_json 

# Load trained model
json_file = open("5_model.json", "r")
loaded_model_json = json_file.read() 
json_file.close()
loaded_model = model_from_json(loaded_model_json)
 
# model weight load 
loaded_model.load_weights("5_weights.h5")
print("Loaded model from disk")

f_name = "folder/test.jpg"  ## change here

test_image = image.load_img(f_name, target_size = (32,32))
test_image = np.array(test_image)
test_image = test_image/255

a_pred = str(loaded_model.predict_classes(test_image.reshape(1,32,32,3)))
o_pred = loaded_model.predict(test_image.reshape(1,32,32,3))
o_pred = np.around(o_pred,3)
pred_100 = o_pred * 100

ind = np.argmax(o_pred, axis = 1)
if o_pred[0,ind] >=0.5 :
    if a_pred == '[0]':
        a_label = '데이지'
    if a_pred == '[1]':
        a_label = '민들레'
    if a_pred == '[2]':
        a_label = '장미'
    if a_pred == '[3]':
        a_label = '해바라기'   
    if a_pred == '[4]':
        a_label = '튤립'  

f = open("folder/result.txt", 'w')  ## change here
f.write(a_label)
f.close()        