from datetime import datetime
from pickle import NONE
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
# from random import uniform
from folium import Marker


class Geopoint(Marker):

    def __init__(self, latitude, longitude, popup=None):
        super().__init__(location=[latitude, longitude], popup=popup)
        self.latitude = latitude
        self.longitude = longitude

    def closest_parallel(self):
        return round(self.latitude)

    def get_time(self):
        timezone_string = TimezoneFinder().timezone_at(
            lat=self.latitude, lng=self.longitude)
        print(timezone_string)
        time_now = datetime.now(timezone(timezone_string))
        return time_now

    def get_weather(self):
        weather = Weather(apikey="26631f0f41b95fb9f5ac0df9a8f43c92",
                          lat=self.latitude, lon=self.longitude)
        return weather.next_12h_simplified()

    # @classmethod
    # def random(cls):
    #     return cls(latitude=uniform(-90, 90), longitude=uniform(-180, 180))


if __name__ == "__main__":
    # tokyo = Geopoint(latitude=35.7, longitude=139.7)
    tokyo = Geopoint(latitude=29.8, longitude=114.3,
                     popup="Hello")  # Location XianNing
    # tokyo = Geopoint(latitude=55.7, longitude=37.6)  # Location moscow
    print(tokyo.closest_parallel())
    print(tokyo.get_time())
    print(tokyo.get_weather())
    # randomGeopoint = Geopoint.random()
    # print(randomGeopoint.latitude, randomGeopoint.longitude)
