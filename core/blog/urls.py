from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView


urlpatterns = [
    path('',PostListView.as_view(),name = 'Blog-Home'),
    path('user/<str:username>/',UserPostListView.as_view(),name = 'user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(),name = 'post-detail'),
    path('post/new/',PostCreateView.as_view(),name = 'post-create'),    #create view template <app>/<model>_form.html
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name = 'post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name = 'post-delete'),
    path('about/', views.about,name='Blog-About'),
]
