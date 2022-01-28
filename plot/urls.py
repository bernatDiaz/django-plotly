from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plot/', views.plot, name='plot'),
    path('data/', views.data, name='data'),
]