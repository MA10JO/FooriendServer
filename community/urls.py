from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList),
    path('<int:pk>/', views.PostDetail),
    path('<int:pk>/comment/', views.CommentDetail)
]