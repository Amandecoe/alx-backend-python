from django.shortcuts import render, HttpResponse
import requests
import datetime
# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'indoor'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=dd2f8a056a0e3b707b8b7838153aba19'

    PARAMS = {'units':'metric'}
    data = request.get(url, PARAMS).json()

    description = data ['weather'][0]['description'] #description of the weather
    icon = data ['weather'][0]['icon'] #description of the weather icon
    temp = data['main']['temp'] #temperature of our city

    day = datetime.date.today()

    return render(request, 'Weatherapp/index.html',{'descritption':description, 'icon':icon, 'temp':temp, 'day':day})
