import sys, os
# settings for the relative path import
sys.path.append(os.path.abspath('..'))
# settings for django, to avoid warnings for uninstalled apps
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokemh.settings')
import requests, json

from scrape import tests
print(tests.y)

import test_im
print(test_im.x)

# settings for avoiding the following error
# django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.
import django
django.setup()

from pokemon.models import *

def scrape():
    base_url = 'https://pokeapi.co/api/v2/'
    for pokemon_id in range(1, 2):
        result = requests.get(f'{base_url}pokemon/{pokemon_id}').text
        result_json = json.loads(result)
        print(result_json.keys())
        print(result_json['name'])
        g1 = Generation(generation_number=1)
        g1.save()


if __name__ == '__main__':
    print(__package__)
    scrape()