import requests
from abc import ABC, abstractmethod
from amadeus import Client, ResponseError
from geopy import geocoders
# import geocoder


class BaseAPI(ABC):
    api_key = ''
    base_url = ''

    @abstractmethod
    def query(self, query_str):
        pass


class RezdyAPI(BaseAPI):
    api_key = '69f708868ddc45eaa1f9b9fad1ddeba5'
    base_url = 'https://api.rezdy.com/'

    def query(self, query_str):
        query = {'apiKey': self.api_key}
        response = requests.get(self.base_url + query_str, params=query)
        return response


class AmadeusAPI(BaseAPI):
    api_key = 'K9OmjVy5Fs3kvWGnE1M37TIogvaLprfG'
    api_secret = '8AHDzdFzt5LaGJ5d'

    def __init__(self):
        self.amadeus_client = Client(
            client_id=self.api_key,
            client_secret=self.api_secret
        )

    def query(self, query_str):

        try:
            gn = geocoders.GeoNames(username='funnnkk')

            location = gn.geocode(query_str)
            response = self.amadeus_client.reference_data.locations.points_of_interest.get(latitude=location.latitude,
                                                                                           longitude=location.longitude)
            return response.data
        except ResponseError as error:
            print(error)
