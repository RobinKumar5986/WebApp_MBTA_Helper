import urllib.request   # urlencode function
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"

# A little bit of scaffolding if you want to use it
def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint(response_data)
    return  response_data

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    url = GMAPS_BASE_URL +'?address=' + place_name
    json_data = get_json(url)
    lat = json_data['results'][0]['geometry']['location']['lat']
    lon = json_data['results'][0]['geometry']['location']['lng']
    return lat, lon




def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.
    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url=MBTA_BASE_URL+ '?api_key='+MBTA_DEMO_API_KEY + \
        '&lat=' + str(latitude) + '&lon=' + str(longitude) + '&format=json'
    station_json=get_json(url)
    station_name=station_json['stop'][0]['stop_name']
    distance=station_json['stop'][0]['distance']
    distance='{:.2f}'.format(float(distance))
    return(station_name, distance)


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and the
    distance from the given place to that stop.
    """
    pass


#Testing
# url = "https://maps.googleapis.com/maps/api/geocode/json?address=Prudential%20Tower"
# get_json(url)
print(get_nearest_station('42.3471477', '-71.0825077'))
