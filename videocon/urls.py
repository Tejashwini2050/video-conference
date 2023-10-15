from . import views
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='singnup'),
    path('signin',views.signin,name='singnin'),
    path('signout',views.signout,name='signout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('meeting',views.videocall,name='meeting'),
    path('join',views.join,name='join')

    
]
