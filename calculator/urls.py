<<<<<<< HEAD
from django.urls import path , include
=======
from django.contrib import admin
from django.urls import path
>>>>>>> refs/remotes/calculator_remote/master
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path ('add', views.add, name = 'add'),
    path ('multiply', views.multiply, name = 'multiply'),
<<<<<<< HEAD
    path('signup',views.signup, name='signup'),
    path('email_confirmation', views.email_confirmation, name='email') ,
    path('db_change_trial', views.db_change_trial, name='db_change_trial2')
=======
    path('tes_page', views.test_page, name = 'tester'),
    path('signup',views.signup, name='signup'),
    path('email_confirmation', views.email_confirmation, name='email')
>>>>>>> refs/remotes/calculator_remote/master
    ]