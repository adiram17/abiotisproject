from typing import Pattern
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('', views.home, name='home'),
    path('test', views.test, name='test'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_password', views.changePassword, name='change_password'),
    
    path('abiotis_list/<type>', views.abiotisList, name='abiotis_list'),
    path('abiotis_create/<type>', views.abiotisCreate, name='abiotis_create'),
    path('abiotis_detail/<type>/<int:id>', views.abiotisDetail, name='abiotis_detail'),
    
]
