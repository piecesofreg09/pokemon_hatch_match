import requests, json
import sys, os
# settings for the relative path import
sys.path.append(os.path.abspath('..'))
# settings for django, to avoid warnings for uninstalled apps
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokemh.settings')

from scrape import tests
print(tests.y)
import test_im
print(test_im.x)

# settings for avoiding the following error
# django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.
import django
django.setup()

from pokemon.models import Generation, Type, Stat, Sprite, Pokemon

def scrape():
    base_url = 'https://pokeapi.co/api/v2/'
    generation_num = 7
    for generation in range(1, generation_num + 1):
        pokemon_num = 2
        g1 = Generation(generation_number=1)
        g1.save()
        for pokemon_id in range(1, max_num):
            result = requests.get(f'{base_url}pokemon/{pokemon_id}').text
            result_json = json.loads(result)
            print(result_json.keys())
            p_name = result_json['name']
            p_weight = result_json['weight']
            


if __name__ == '__main__':
    print(__package__)
    Generation.objects.all().delete()
    Type.objects.all().delete()
    Stat.objects.all().delete()
    Sprite.objects.all().delete()
    Pokemon.objects.all().delete()
    scrape()