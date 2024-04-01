from django.urls import path
from . import views

urlpatterns = [
    path('', views.convertor_view, name='convertor_view'),
    path('generate_html/', views.generate_html, name='generate_html'),
]