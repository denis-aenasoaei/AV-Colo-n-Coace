import requests
from abc import ABC, abstractmethod
from amadeus import Client, ResponseError
from geopy import geocoders
import os
from requests.exceptions import HTTPError
from requests.structures import CaseInsensitiveDict
import json


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


class GeoNamesAPI(BaseAPI):
    def query(self, query_str):
        response = []
        with open(os.path.abspath('..\\RO.txt'), 'r',
                  encoding='utf8') as file:
            for line in file.readlines():
                response.append(line.split('\t'))
        for respons in response:
            if respons[1] == query_str:
                return respons
        return None


class MeteoAPI(BaseAPI):
    api_key = '288db9dbe1824ff4936175122222305'
    base_url = 'http://api.weatherapi.com/v1/current.json'

    def query(self, city):
        try:

            print('Looking for the weather in', city, '...')
            query = {'key': self.api_key,
                     'Protocol': 'HTTP',
                     'Format': 'JSON',
                     'q': city}
            response = requests.get(self.base_url, params=query)
            response = dict(response.json())
            return response['current']['temp_c'], response['current']['condition']['text']

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'An error occurred: {err}')


class MapAPI(BaseAPI):
    api_key = '554afae1313b40ce9ffa2ccbbee17cc8'
    base_url = 'https://api.geoapify.com/v1/routing'

    def query(self, coordinates):
        query = {'apiKey': self.api_key,
                 'waypoints': f'{str(coordinates[0])},{str(coordinates[1])}|'
                              f'{str(coordinates[2])},{str(coordinates[3])}',
                 'mode': 'drive'}

        headers = CaseInsensitiveDict()
        headers['Accept'] = 'application/json'

        response = requests.get(self.base_url, headers=headers, params=query)
        response = dict(response.json())

        distance_in_km = response['features'][0]['properties']['distance'] / 1000.0

        return f'There are {distance_in_km} km between them.'
