from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.get_info),
    path('post_info',views.post_info),
]
