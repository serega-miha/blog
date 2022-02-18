from django.urls import path
from .views import MainView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', MainView.as_view(), name='index'),
]