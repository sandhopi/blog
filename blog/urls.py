from django.urls import path, include
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add_blog', views.add_blog, name='add_blog'),
    path('<id>', views.detail, name='detail'),
    path('add/perfom', views.add_perfom, name='add_perfom'),

]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)