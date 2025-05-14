from django.urls import path
from search_result import views

urlpatterns = [
    path('', views.result, name='result'),
    path('<int:cat>/', views.category_blog, name='category_blog'),
]
