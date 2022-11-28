from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList),
    path('<int:pk>/', views.PostDetail),
    path('comment/', views.CommentDetail),
    path('categories/<int:pk>/', views.CategoryPostList),
    path('categories/', views.CategoryList)
]