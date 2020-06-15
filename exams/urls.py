from django.urls import path
from . import views

urlpatterns = [
    path('exam01', views.exam01, name='exam01'),
    path('exam02', views.exam02, name='exam02'),
    path('exam03', views.exam03, name='exam03'),
    path('exam04', views.exam04, name='exam04'),
    path('exam05', views.exam05, name='exam05'),
    path('exam06', views.exam06, name='exam06'),
    path('exam07', views.exam07, name='exam07'),
    path('exam08', views.exam08, name='exam08'),
]
