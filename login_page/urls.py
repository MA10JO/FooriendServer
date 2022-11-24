from django.urls import path

import login_page
from . import views

urlpatterns = [ #http://127.0.0.1:8000/#login_page/
    path('login/', login_page.views.login, name='login'),
    path('signup/', login_page.views.signup, name='signup'),
    path('logout/', login_page.views.logout, name='logout'),
]