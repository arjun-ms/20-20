#All Logic of Prediction Should be Here 
#This Function Should Only Return The Result of Prediction (Mammooty or Mohanlal)

import numpy as np
import cv2
import keras

#Image Preprocessing
def image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    new_arr = cv2.resize(img, (224, 224))
    new_arr = np.array(new_arr)
    new_arr = new_arr.reshape(-1, 224,224, 1)
    return new_arr

#Return Prediction
def predict(file_path):
    CATEGORIES = ['mammooty', 'mohanlal']
    model = keras.models.load_model('cnn3.model')
    result = model.predict([image(file_path)])
    if result[0][0] == 1:
        prediction = 'mamooty'
    elif result[0][0] == 0:
        prediction = 'mohanlal'
    else:
        prediction = 'I dont know this guy!'
    return prediction
