import os
import spacy
from geopy.geocoders import Nominatim


def cityEntity(query):
    location = locations_from_Romania(query, flag=1)
    if len(location) == 2:
        return location[1]
    elif len(location) == 1:
        return location[0]

    NER = spacy.load("en_core_web_sm")
    response = NER(query)

    for word in response.ents:
        if word.label_ == "GPE":
            return word.text

    return 0


def locations_from_Romania(query, flag):
    file_content = []
    with open(os.path.join('C:\\Users\\Camelia\\Documents\\GitHub\\AV-Colo-n-Coace\\dialog_system\\info_system',
                           'RO.txt'), 'r', encoding='utf8') as file:
        for line in file.readlines():
            file_content.append(line.split('\t'))

    cities = []
    for location_list in file_content:
        if len(cities) < 2:
            if location_list[1] in query and location_list[1] not in cities:
                cities.append(location_list[1])
                if flag == 1:
                    cities.append(location_list[2])
            elif location_list[2] in query and location_list[2] not in cities:
                cities.append(location_list[2])
        else:
            break

    return cities


def find_waypoints(query):
    NER = spacy.load("en_core_web_sm")
    response = NER(query)

    cities = []
    for word in response.ents:
        if word.label_ == "GPE":
            cities.append(word.text)

    if len(cities) < 2:
        cities = locations_from_Romania(query, flag=2)
        print(cities)

    waypoints = []
    geolocator = Nominatim(user_agent="AV_proj")
    if len(cities) == 2:
        for city in cities:
            location = geolocator.geocode(city)
            waypoints.append(location.latitude)
            waypoints.append(location.longitude)
    elif len(cities) == 4:
        city1 = cities[0]
        country1 = cities[1]
        location1 = geolocator.geocode(city1 + ',' + country1)
        waypoints.append(location1.latitude)
        waypoints.append(location1.longitude)

        city2 = cities[2]
        country2 = cities[3]
        location2 = geolocator.geocode(city2 + ',' + country2)
        waypoints.append(location2.latitude)
        waypoints.append(location2.longitude)

    if len(waypoints) == 4:
        return waypoints
    else:
        return 0
