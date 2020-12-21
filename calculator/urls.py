
from django.urls import path , include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path ('add', views.add, name = 'add'),
    path('signup',views.signup, name='signup'),
    path('email_confirmation', views.email_confirmation, name='email') ,
    #path('db_change_trial', views.db_change_trial, name='db_change_trial2'),
    path('signup',views.signup, name='signup'),
    path('email_confirmation', views.email_confirmation, name='email')
    ]