from folium import Map, Popup
from geo import Geopoint

# Get latitude and longitude values
# latitude = -29.8
# longitude = -65.7
locations = [[-29.8, -65.7], [-30.8, -67.7], [-27.8, -62.7], [-32, -70]]

# Folium Map instance
myMap = Map(location=[29.8, 114])

for latitude, longitude in locations:
    antipode_latitude = latitude * -1

    if longitude <= 0.0:
        antipode_longitude = longitude + 180.0
    elif longitude > 180.0:
        antipode_longitude = "Invalid Longitude"
    else:
        antipode_longitude = longitude - 180.0

    # Create a Geopoint instance
    geopoint = Geopoint(latitude=antipode_latitude,
                        longitude=antipode_longitude)

    forecast = geopoint.get_weather()

    popup_content = f"""
    {forecast[0][0][-8:-6]}h: {round(forecast[0][1])}℉ <img src="http://openweathermap.org/img/wn/{forecast[0][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[1][0][-8:-6]}h: {round(forecast[1][1])}℉ <img src="http://openweathermap.org/img/wn/{forecast[1][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[2][0][-8:-6]}h: {round(forecast[2][1])}℉ <img src="http://openweathermap.org/img/wn/{forecast[2][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[3][0][-8:-6]}h: {round(forecast[3][1])}℉ <img src="http://openweathermap.org/img/wn/{forecast[3][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    """
    popup = Popup(popup_content, max_width=400)
    popup.add_to(geopoint)

    geopoint.add_to(myMap)


myMap.save("antipode.html")
