from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name="home"),
       path('download_excel/', views.download_excel, name="download_excel"),
]