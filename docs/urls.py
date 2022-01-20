from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from docs.views import index, signup, loginUser, signout, dsa

urlpatterns = [
    path('',index, name='index'),
    path('signup/',signup, name='signup'), 
    path('loginUser/',loginUser, name='loginUser'),
    path('signout/',signout, name='signout'),
    path('dsa/',dsa),
    # path('oops/',oops),
    # path('cg/',cg),
]