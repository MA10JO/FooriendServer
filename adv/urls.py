from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.PostList.as_view()),
=======
    path('', views.PostList),
    path('comment/', views.CommentList),
>>>>>>> origin/main
    path('<int:pk>/', views.PostDetail.as_view()),
    #path('create_post/', views.PostCreate.as_view()),
    #path('category/<str:slug>/', views.category_page)
]