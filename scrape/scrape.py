import requests, json

from . import tests
print(tests.y)

from .. import test
print(test.x)

from ..pokemon.models import *

def scrape():
    base_url = 'https://pokeapi.co/api/v2/'
    for pokemon_id in range(1):
        result = requests.get(f'{base_url}pokemon/{pokemon_id}').text
        result_json = json.loads(result)
        print(result_json.keys())
        print(result_json['name'])


if __name__ == '__main__':
    scrape()