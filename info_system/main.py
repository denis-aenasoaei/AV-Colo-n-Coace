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

    return api_caller.query(city)
