from django.shortcuts import render
from calculator.models import extended, otp_data
from .models import price_data
from django.http import HttpResponse
from django.core.management import call_command
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from calculator.models import extended, otp_data

xyz = extended.objects.filter(username='aaa5')

def login(request):
    if request.method == 'POST':
      username1 = request.POST['username']
      password1 = request.POST['password']
      User = auth.authenticate(username=username1, password=password1)

      if User is not None:  #if the authenticate function does pass the authentication , it will return none
        auth.login(request,User)
        #return render(request, 'showdata.html')
        return render(request, 'price_input.html')  # this will call the other function
      else:
        return render(request, 'auth_failed.html')
        
    else:
      #return render(request, 'auth_failed.html')
      return render(request, 'login_page.html', {'login': 'http://127.0.0.1:8000/venu/price_input'}) # use full address when in diff app


def price_input(request):
    
    if request.method == 'POST':
        price_data_in = request.POST['price_input_html']
        y = price_data(price=price_data_in)
        y.save()
        print("price input done")
        return render(request, 'Thank_you.html')
        
    else:
        return render(request, 'price_input.html')


def homepage(request):
    #xyz = extended.objects.filter(username='aaa5')
    #return render(request, 'venu_home.html', {'price':x ,'username':xyzout1 })
    Today_price = price_data.objects.order_by('-id')[:1]
    #Last_7_days = price_data.objects.order_by('-id')[0:7]
    Last_7_days = price_data.objects.order_by('-id')[0:7] 

    for i in Today_price: 
        today=i.price
    print(today)

    out = []
    for i in Last_7_days:
        out.append(i.price)
    print(out)


    return render(request, 'venu_home.html', {'price_2': today , 'last_7_days': out })
