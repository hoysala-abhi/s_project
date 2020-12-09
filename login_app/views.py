from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.
def login(request):
    if request.method == 'POST':
      username1 = request.POST['username']
      password1 = request.POST['password']
      y = auth.authenticate(username=username1, password=password1)

      if y is not None:
        auth.login(request,y)
        return redirect('/')
      else:
        return render(request, 'auth_failed.html')

    else:
      return render(request, 'login_page.html', {'login': 'http://127.0.0.1:8000/login'})

def logout(request):
    auth.logout(request)
    return redirect('/')