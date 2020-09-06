# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/9/2
from django.urls import path

from . import views

urlpatterns = [
    path('', views.qipaoshui),
    path('index', views.qipaoshui),
    path('qipaoshui', views.qipaoshui)
]