from info_system.API import BaseApi
from info_system import cityEntity


def queryApp(query):
    # api_caller = BaseApi.AmadeusAPI()
    api_caller = BaseApi.GeoNamesAPI()
    city = cityEntity.cityEntity(query)

    if city == 0:
        return
    if query.lower() == 'stop':
        exit(0)

    resp = api_caller.query(city)

    return resp