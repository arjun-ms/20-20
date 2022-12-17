#All Logic of Prediction Should be Here
#This Function Should Only Return The Result of Prediction (Mammooty or Mohanlal)

import numpy as np
import cv2
import keras

#Image Preprocessing
def image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    new_arr = cv2.resize(img, (224, 224))
    new_arr = np.array(new_arr)/255
    new_arr = new_arr.reshape(-1, 224,224, 1)
    return new_arr

#Return Prediction
def predict(file_path):
    CATEGORIES = ['mammooty', 'mohanlal','random']
    model = keras.models.load_model('3-class-improved.h5')
    result = model.predict([image(file_path)])
    if result[0][0] > result[0][1] and result[0][0] > result[0][2]:
        prediction = 'Mammootty'
    elif result[0][1] > result[0][0] and result[0][1] > result[0][2]:
        prediction = 'Mohanlal'
    else:
        prediction = 'I dont know this guy!'
    return prediction