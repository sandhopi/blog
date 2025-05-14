from django.urls import path, include
from account import views

app_name = 'account'

urlpatterns = [
    path('daftar', views.sign_up, name='sign_up'),
    path('masuk', views.sign_in, name='sign_in'),
    path('activate/<uidb64>/<token>/', views.activate , name='activate'),
    path('log_out', views.log_out , name='log_out'),
    
]
