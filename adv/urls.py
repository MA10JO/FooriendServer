from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList),
    path('comment/', views.CommentList)
    #path('create_post/', views.PostCreate.as_view()),
    #path('category/<str:slug>/', views.category_page)
]