import requests
import json
from secrets import WEATHER_API_KEY
from secrets import BASE_URL




class WeatherCaller():
    def __init__(self ,city_name):
        self.city_name = city_name

    

    def get_wind_degree(self):
        
        
        api_call = f'{BASE_URL}?key={WEATHER_API_KEY}&q={self.city_name}&aqi=no'
        response = requests.get(api_call)
        
        data = json.loads(response.text)
        print(data['current']['wind_degree'])
    
    def get_coordinates(self):

        api_call = f'{BASE_URL}?key={WEATHER_API_KEY}&q={self.city_name}&aqi=no'
        response = requests.get(api_call)

        data = json.loads(response.text)
        coordinates = ( data['location']['lat'] ,data['location']['lon'] )
        print(coordinates)



london_caller = WeatherCaller('London')

london_caller.get_wind_degree()
london_caller.get_coordinates()