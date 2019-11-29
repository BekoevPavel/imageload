
from django.conf.urls import url, include
from django.contrib import admin
from . import views

from .views import HomePageView
urlpatterns = [
    url('', HomePageView.as_view(), name='home'),
]