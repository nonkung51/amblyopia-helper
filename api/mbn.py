from keras.preprocessing import image
from keras.applications.mobilenet import (preprocess_input, MobileNet,
                                          decode_predictions)
import numpy as np
import pickle, fire

dictionary = pickle.load(open('dict.p', 'rb'))

model = MobileNet(input_shape=None, alpha=1.0, depth_multiplier=1,
                  dropout=1e-3, include_top=True,
                  weights='imagenet', input_tensor=None,
                  pooling=None, classes=1000)

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
