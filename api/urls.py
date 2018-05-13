from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Home),
    url(r'^ocr/$', views.predictOcrAPIView.as_view()),
    url(r'^mbn/$', views.predictMbnAPIView.as_view())
]
