from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path ('add', views.add, name = 'add'),
    path ('multiply', views.multiply, name = 'multiply'),
    path('tes_page', views.test_page, name = 'tester'),
    path('GM',views.wish),
    path('signup',views.signup, name='signup'),
    path('email', views.email_confirmation, name='email')
    ]