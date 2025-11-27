from django.shortcuts import render #render allows django to send data to a template (HTML)
import requests #python library used to call external APIs
import datetime #used to get today's date

def home(request):
    # city from form, tries to get the value the user typed in the form <input name = "city">
    #if user haven't submitted anything the default is Addis Ababa
    #this ensures the app doesnt fail the first time it loads
    city = request.POST.get('city', 'Addis Ababa')

    url = 'https://api.openweathermap.org/data/2.5/weather' #API url, where we send our request
    params = { #parameters for the request to be sent
        'q': city, #tells the API "give weather for this city"
        'appid': 'dd2f8a056a0e3b707b8b7838153aba19', #Personal API key
        'units': 'metric' #temperature in C
    }

    data = requests.get(url, params=params).json() #sends a GET request, converts the response from JSON text and stores it onto "data"
    print(data)   # ← for debugging, shows RAW API in terminal

    # ❗ If city not found or API error, avoid KeyError
    if data.get("cod") != 200: #if API returns "cod" as status code, 200 means success, any other code is not success
        return render(request, 'Weatherapp/index.html', {
            'error': data.get('message', 'Unknown error'), #shows the error message rather than crashing the server
            'day': datetime.date.today() #even if there is an error it still renders your page with the date
        })

    # Extract safely
    description = data['weather'][0]['description'] # a list containing weather info, [0] the first item on the list , [description] weather description
    icon = data['weather'][0]['icon'] #icon code
    temp = data['main']['temp']#actual temperature, these keys exist if only the API returned cod=200

    day = datetime.date.today() #Gets today's date

    return render(request, 'Weatherapp/index.html', {
        'description': description,
        'icon': icon,
        'temp': temp,
        'city': city,
        'day': day
    }) #this renders out html page, sends all data to the frontend
