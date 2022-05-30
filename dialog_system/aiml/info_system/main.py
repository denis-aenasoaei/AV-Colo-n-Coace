from info_system.API import BaseApi
from info_system import cityEntity


def queryApp(query):
    api_caller = BaseApi.GeoNamesAPI()
    city = cityEntity.cityEntity(query)

    if city == 0:
        return
    if query.lower() == 'stop':
        exit(0)

    return api_caller.query(city)


def meteo_query(query):
    api_caller = BaseApi.MeteoAPI()
    city = cityEntity.cityEntity(query)

    if city == 0:
        return
    if query.lower() == 'stop':
        exit(0)

    temp_c, condition = api_caller.query(city)

    return f"There are {temp_c} Celsius degrees: {condition}."


def map_query(query):
    api_caller = BaseApi.MapAPI()
    coordinates = cityEntity.find_waypoints(query)

    if coordinates == 0:
        return
    if query.lower() == 'stop':
        exit(0)

    return api_caller.query(coordinates)
