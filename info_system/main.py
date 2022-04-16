from info_system.API import BaseApi
from info_system import cityEntity

def queryApp(query):

    api_caller = BaseApi.AmadeusAPI()
    # while 1:
        # query = input("Please provide a query or type stop to finish session:\n")

    city = cityEntity.cityEntity(query)
    if query.lower() == 'stop':
        exit(0)
    resp = api_caller.query(city)
    return resp


# if __name__ == '__main__':
#     main()

