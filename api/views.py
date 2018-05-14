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

def translate(text):
    return dictionary[text]

def ocr(name):
    print('requesting OCR...')
    return pytesseract.image_to_string(Image.open(name), lang='tha')

def mbn(name):
    print('requesting...')
    console = 'python3 api/mbn.py mbn \'{0}\''.format(name)
    out = os.popen(console).readlines()[0][0:-1]

    return out

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
