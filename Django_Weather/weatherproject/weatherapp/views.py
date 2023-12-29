from django.shortcuts import render
import requests
import datetime

# Create your views here.
def home(request):
    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = 'ahmedabad'     
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=392536ff739663854f38d89573454355'
    PARAMS = {'units':'metric'}

    data = requests.get(url,PARAMS).json()
    
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']
    day = datetime.date.today()

    return render(request,'home.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city })
    