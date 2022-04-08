import urllib.parse
import requests
from shapely.geometry import Point, Polygon
import csv


def localisation(address):
    try:
        address_encoded = urllib.parse.urlencode({'q': address})
        response = requests.get('https://api-adresse.data.gouv.fr/search/?q='+address_encoded)
        response.raise_for_status()
    except requests.RequestException:
        return None

    try:
        all_data = response.json()
        return {
            "coordinates": all_data["features"][0]["geometry"]["coordinates"]
        }
    except (KeyError, TypeError, ValueError):
        return None


def circonscription(lon, lat):
    # Create Point objects
    point = Point(lon, lat)

    # reading csv and making list of dict of circonscriptions
    with open('circonscriptions.csv', mode='r') as inp:
        reader = csv.reader(inp)
        circonscriptions = [{'name':row[0],'loc':(row[1])} for row in reader]

    # Split string into a list
    for circonscription in circonscriptions:
        circonscription['loc'] = circonscription['loc'].split()
        # Turning list of string into list of float
        circonscription['loc'] = [float(i) for i in circonscription['loc']]
        # Making duo tuples (lon, lat)
        it = iter(circonscription['loc'])
        circonscription['loc'] = list(zip(it,it))

    # Look for the circonscription that contains our point
    longeur=len(circonscriptions)
    for x in range(0, longeur):
        if point.within(Polygon(circonscriptions[x]['loc'])):
            return str(circonscriptions[x]['name'])
    


