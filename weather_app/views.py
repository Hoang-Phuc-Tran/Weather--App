from django.shortcuts import render, redirect, get_object_or_404
import requests
from .models import City
from .forms import CityForm
from django.http import HttpResponse

def index(request):
    API_KEY = 'b7331135c7544f4526e4aa20e9667ca6'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'

    cities = City.objects.all().order_by('-updated_at') #return all the cities in the database
    
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        city_validate = requests.get(url.format(request.POST['name'], API_KEY)).json() #request the API data and convert the JSON to Python data 
        # validate if the city is valid in the api website openweathermap.org
        if city_validate['cod'] == 200:
            form.save()
        
    form = CityForm()
    
    weather_data = []
    
    for city in cities:

        city_weather = requests.get(url.format(city, API_KEY)).json() #request the API data and convert the JSON to Python data types
        
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list

    context = {'weather_data' : weather_data, 'form': form}

    return render(request, 'template_app/index.html', context) #returns the index.html template

# Delete search History
def deleteCity(request):
    
    city = City.objects.all().delete()
    
    return redirect('home')