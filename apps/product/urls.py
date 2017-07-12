from django.conf.urls import url
from django.conf.urls import include 

from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    url(r'^products/maxndvi/', views.MaxNdviView.as_view()),
]