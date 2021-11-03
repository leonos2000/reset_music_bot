
from django.urls import path

from . import views

urlpatterns = [
  path('', views.mainView),
  path('reboot/', views.rebootView),
]