from django.urls import path

from . import views  # import all 

urlpatterns = [
    path('', views.index, name='index')
]