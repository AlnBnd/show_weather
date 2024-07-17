import requests
import os
import pytz
from datetime import datetime, timezone
from django.shortcuts import render
from .forms import CityForm
from .models import City
from geopy.geocoders import Nominatim


def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="weather")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    return None, None

def get_weather(latitude, longitude):
    weather_data = []
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        times = data['hourly']['time']
        temperatures = data['hourly']['temperature_2m']
 
        current_time = datetime.now(timezone.utc)
        for time, temp in zip(times, temperatures):
            forecast_time = datetime.fromisoformat(time).replace(tzinfo=pytz.utc)
            if forecast_time > current_time:
                weather_data.append((forecast_time, temp))
        return weather_data[3:]
    return None

def index(request):
    weather_data = None
    city_name = ''
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city_name']
            latitude, longitude = get_coordinates(city_name)
            if latitude and longitude:
                weather_data = get_weather(latitude, longitude)
                City.objects.create(city_name=city_name)
    else:
        form = CityForm()

    context = {
        'form': form,
        'weather_data': weather_data,
        'city_name': city_name,

    }
    return render(request, 'index.html', context)