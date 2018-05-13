from keras.preprocessing import image
from keras.applications.mobilenet import (preprocess_input, MobileNet,
                                          decode_predictions)
from keras.applications import mobilenet
from keras.models import load_model
import numpy as np
import pickle, fire

dictionary = pickle.load(open('dict.p', 'rb'))

model = load_model('mobilenet.h5', custom_objects={
                   'relu6': mobilenet.relu6,
                   'DepthwiseConv2D': mobilenet.DepthwiseConv2D})

model.load_weights('my_model_weights.h5')

class MobileNet():
    def mbn(self, name):
        img_path = name
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)

        x = preprocess_input(x)
        features = model.predict(x)
        preds = decode_predictions(features, top=1)[0]
        english_prediction = preds[0][1]

        return dictionary[english_prediction]

if __name__ == '__main__':
    fire.Fire(MobileNet)
