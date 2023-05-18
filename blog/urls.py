from django.urls import path

from . import views



urlpatterns = [
    path('search/', views.search, name='search'),
    path('category/<slug:slug>/', views.category, name='category_detail'),
    path('<str:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'), 
] 