from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('home/', views.home, name='app-home'),
    path('upload/', views.upload, name='app-upload'),
    path('download/', views.download, name='app-download'),
    # path('about/', views.about, name='blog-about'),
]
