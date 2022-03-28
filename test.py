from shapely.geometry import Point, Polygon
import csv

# Create Point objects
point = Point(2.4180191227510135, 48.868372628437285)


# reading csv and making list of dict of circonscriptions
with open('/Users/arthur/Documents/MyCode/TrouverVotreDéputé.fr/circonscriptions.csv', mode='r') as inp:
    reader = csv.reader(inp)
    # next(reader, None)
    circonscriptions = [{'name':row[0],'loc':(row[1])} for row in reader]

# Split string into a list
for circonscription in circonscriptions:
    circonscription['loc'] = circonscription['loc'].split()
    # Turning list of string into list of float
    circonscription['loc'] = [float(i) for i in circonscription['loc']]
    # Making duo tuples (lon, lat)
    it = iter(circonscription['loc'])
    circonscription['loc'] = list(zip(it,it))

longeur=len(circonscriptions)
for x in range(0, longeur):
    if point.within(Polygon(circonscriptions[x]['loc'])):
        print(str(circonscriptions[x]['name']))