from django.urls import path, include
from beranda import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kategori', views.kategori, name='kategori')
]
