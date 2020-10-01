from django.urls import path
from . import views

urlpatterns = [
        path('',views.testapp, name='testapp'),
        path('OTP',views.OTP, name='testapp1')

    ]