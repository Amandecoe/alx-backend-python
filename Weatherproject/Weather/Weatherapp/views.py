from django.shortcuts import render
import requests
import datetime

def home(request):
    # city from form
    city = request.POST.get('city', 'Addis Ababa')

    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': 'dd2f8a056a0e3b707b8b7838153aba19',
        'units': 'metric'
    }

    data = requests.get(url, params=params).json()
    print(data)   # ← for debugging

    # ❗ If city not found or API error, avoid KeyError
    if data.get("cod") != 200:
        return render(request, 'Weatherapp/index.html', {
            'error': data.get('message', 'Unknown error'),
            'day': datetime.date.today()
        })

    # Extract safely
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']

    day = datetime.date.today()

    return render(request, 'Weatherapp/index.html', {
        'description': description,
        'icon': icon,
        'temp': temp,
        'city': city,
        'day': day
    })
