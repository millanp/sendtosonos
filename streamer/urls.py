from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<yturl>[\w-]+)$', views.add_to_mp3_stream)
]
