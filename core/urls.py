from django.urls import path

from . import views

urlpatterns = [
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('', views.frontpage, name='frontpage'),
    path('about/', views.about, name='about'),   
] 