import spacy
from geopy.geocoders import Nominatim


def cityEntity(query):
    NER = spacy.load("en_core_web_sm")
    response = NER(query)

    for word in response.ents:
        if word.label_ == "GPE":
            return word.text

    return 0


def find_waypoints(query):
    NER = spacy.load("en_core_web_sm")
    response = NER(query)
    print(response.ents)

    # if len(response.ents) < 2:
    #     NER = spacy.load('ro_core_news_sm')
    #     response = NER(query)
    #     print(response.ents)

    cities = []
    for word in response.ents:
        if word.label_ == "GPE":
            cities.append(word.text)

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
