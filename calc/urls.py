from django.urls import path

from . import views  # import all 

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add')
]