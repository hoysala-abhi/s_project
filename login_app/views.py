from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from calculator.models import extended, otp_data


# Create your views here.
def login(request):
    if request.method == 'POST':
      username1 = request.POST['username']
      password1 = request.POST['password']
      User = auth.authenticate(username=username1, password=password1)

      if User is not None:  #if the authenticate function does pass the authentication , it will return none
        auth.login(request,User)
        #return render(request, 'showdata.html')
        return showdata(request)  # this will call the other function
      else:
        return render(request, 'auth_failed.html')
        
    else:
      #return render(request, 'auth_failed.html')
      return render(request, 'login_page.html', {'login': 'http://127.0.0.1:8000/login'}) # use full address when in diff app

@login_required(login_url='/login_app/login/')  # Decorator : add condition for below function.#logged in user is saved in the cache
def showdata(request):      #this is to show the data of the logged-in user. 
    #datas = extended.objects.filter(username=request.username)
    datas = extended.objects.filter(username='aaa5')
    return render(request, 'showdata.html', {'data':datas })

def logout(request):
    auth.logout(request)
    return redirect('/') 