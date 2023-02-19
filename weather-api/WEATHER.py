from unicodedata import name
import requests


class city:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=3009005ca09ba1e7341face27474569a")

        except:
            print("sorry you don't have internet connection")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]
        self.name = name

    def temp_print(self):
         units_symbol = "c"
         if self.units =="imperial":
              units_symbol= "F"
         print(f"in {name} it is currently {self.temp} {units_symbol}")
         print(f"today's hight {self.temp_max} {units_symbol}")
         print(f"today's low {self.temp_min} {units_symbol}")

name = "karachi"
my_city = city("karachi", 24.8607, 67.0011)
my_city.temp_print()
name = "islamabad"
my_city2 = city("islamabad", 33.6844, 73.0479,units="imperial")
my_city2.temp_print()
print(my_city2.response_json)