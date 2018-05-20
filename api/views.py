import pytesseract
from PIL import Image

import os

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ImageSerializer

from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

from keras.preprocessing import image
from keras.applications.mobilenet import (preprocess_input, MobileNet,
                                          decode_predictions)
import numpy as np
import pickle

global model
model = MobileNet(input_shape=None, alpha=1.0, depth_multiplier=1,
                  dropout=1e-3, include_top=True,
                  weights='imagenet', input_tensor=None,
                  pooling=None, classes=1000)
model._make_predict_function()

def ocr(name):
    print('requesting OCR...')
    return pytesseract.image_to_string(Image.open(name), lang='tha')

def mbn(name):
    print('requesting MBN...')
    dictionary = pickle.load(open('dict.p', 'rb'))
    img_path = name
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    x = preprocess_input(x)
    features = model.predict(x)
    preds = decode_predictions(features, top=1)[0]
    english_prediction = preds[0][1]

    return dictionary[english_prediction]

def Home(request):
    return HttpResponse('<h1>it\'s working!</h1>')

class predictOcrAPIView(APIView):
    def get(self, request):
        return Response([])
    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            img = request.data['image']
            path = default_storage.save('temp.jpg', ContentFile(img.read()))
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)
            print('OCR is working..')
            ocr_ = ocr(tmp_file)
            os.remove(tmp_file)
            return Response({'OCR': ocr_})
        return Response({'Success': 0})

class predictMbnAPIView(APIView):
    def get(self, request):
        return Response([])
    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            img = request.data['image']
            path = default_storage.save('temp.jpg', ContentFile(img.read()))
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)
            print('Getting in network...')
            mbn_ = mbn(tmp_file)
            os.remove(tmp_file)
            return Response({'MBN': mbn_})
        return Response({'Success': 0})
