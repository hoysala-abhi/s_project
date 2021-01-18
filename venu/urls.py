from django.urls import path
from . import views

urlpatterns = [
        path('homepage', views.homepage, name='homepage'),
        path('price_input', views.price_input, name='price_input'),
        path('login', views.login, name='login')
    ]