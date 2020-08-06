import requests, json
import sys, os
from urllib.request import urlopen
from bs4 import BeautifulSoup
# settings for the relative path import
sys.path.append(os.path.abspath('..'))
'''
from scrape import tests
print(tests.y)
import test_im
print(test_im.x)
'''

# settings for django, to avoid warnings for uninstalled apps
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokemh.settings')

# settings for avoiding the following error
# django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.
import django
django.setup()

from pokemon.models import Generation, Type, Stat, Sprite, Pokemon

def scrape():
    base_url = 'https://pokeapi.co/api/v2/'
    generation_num = 1
    for generation in range(1, generation_num + 1):
        gen_obj = Generation(generation_number=generation)
        gen_obj.save()

        result_gen = requests.get(f'{base_url}generation/{generation}').text
        result_gen_json = json.loads(result_gen)
        pokemons = result_gen_json['pokemon_species']
        
        for pokemon in pokemons[:2]:
            # species information
            url = pokemon['url'][:-1]
            pokemon_name = pokemon['name']
            result_species = requests.get(f'{base_url}pokemon-species/{pokemon_id}').text
            result_species_json = json.loads(result_species)

            # pokemon information
            pokemon_id = url[len(url) - url[::-1].index('/'):]
            result = requests.get(f'{base_url}pokemon/{pokemon_id}').text
            result_json = json.loads(result)

            p_name = result_json['name']
            p_weight = int(result_json['weight'])
            p_height = int(result_json['height'])
            p_base_exp = int(result_json['base_experience'])
            p_capture_rate = int(result_species_json['capture_rate'])
            p_cost = 1000 // p_capture_rate

            # sprites information
            back_default = result_json['sprites']['back_default']
            front_default = result_json['sprites']['front_default']
            svg_sprite = result_json['sprites']['other']['dream_world']['front_default']
            
            # big sprite extraction
            sprite_page_external_url = f'https://bulbapedia.bulbagarden.net/wiki/{p_name}'
            sprite_bs = BeautifulSoup(requests.get(sprite_page_external_url).text, 'html.parser')
            p_name_cap = p_name.capitalize()
            sprite_url = sprite_bs.select("img[alt=\"{p_name_cap}\"]")[0]['src']
            sprite_url = 'http:' + sprite_url

            # sprites object
            sprite_obj = Sprite(back_default=back_default, front_default=front_default,
                svg_sprite=svg_sprite, big_sprite=sprite_url)
            sprite_obj.save()

            # stat information
            stats = result_json['stats']
            key_name = 'base_stat'
            hp = stats[0][key_name]
            attack = stats[1][key_name]
            defense = stats[2][key_name]
            special_attack = stats[3][key_name]
            special_attack_acc_rounds = ((special_attack - attack) / attack) // 0.5 + 1
            special_defense = stats[4][key_name]
            speed = stats[5][key_name]

            # stat object
            stat_obj = Stat(hp=hp, attack=attack, defense=defense,
                special_attack=special_attack, 
                special_attack_acc_rounds=special_attack_acc_rounds,
                special_defense=special_defense, speed=speed)
            stat_obj.save()

            p_obj = Pokemon(idd=pokemon_id, name=p_name,
                weight=p_weight, height=p_height, base_exp=p_base_exp,
                cost=p_cost, user_defined=True, generation=gen_obj,
                sprites=sprite_obj, stat=stat_obj)
            p_obj.save()

            for type_n in result_json['types']:
                name = type_n['name']
                
                type_obj = Type()

def type_scrape():
    print('in type scraping')
    base_url = 'https://pokeapi.co/api/v2/'
    result_types = requests.get(f'{base_url}type').text
    json_types = json.loads(result_types)
    print('in base type scraping')
    for count, type_pair in enumerate(json_types['results']):
        print(count)
        type_url = type_pair['url']
        result_type = requests.get(type_url).text
        json_type = json.loads(result_type)
        idd = int(json_type['id'])
        name = json_type['name']
        t1 = Type(type_number=idd, name=name)
        t1.save()
    print('done base type scraping')
    print('in related type scraping')
    for count, type_pair in enumerate(json_types['results']):
        #print(count)
        type_url = type_pair['url']
        result_type = requests.get(type_url).text
        json_type = json.loads(result_type)
        idd = int(json_type['id'])
        main_type = Type.objects.get(pk=idd)
        #print(main_type)

        damage_rel = json_type['damage_relations']
        #print(damage_rel)
        # double damage from
        for type_pair in damage_rel['double_damage_from']:
            link_type = Type.objects.get(name=type_pair['name'])
            main_type.double_damage_from.add(link_type)
        
        # double damage to
        for type_pair in damage_rel['double_damage_to']:
            link_type = Type.objects.get(name=type_pair['name'])
            main_type.double_damage_to.add(link_type)
        
        # half damage from
        for type_pair in damage_rel['half_damage_from']:
            link_type = Type.objects.get(name=type_pair['name'])
            main_type.half_damage_from.add(link_type)
        
        # half damage to
        for type_pair in damage_rel['half_damage_to']:
            link_type = Type.objects.get(name=type_pair['name'])
            main_type.half_damage_to.add(link_type)
        
        # no damage from
        for type_pair in damage_rel['no_damage_from']:
            link_type = Type.objects.get(name=type_pair['name'])
            main_type.no_damage_from.add(link_type)
        
        # no damage to
        for type_pair in damage_rel['no_damage_to']:
            link_type = Type.objects.get(name=type_pair['name'])
            main_type.no_damage_to.add(link_type)
    print('Done scraping relationships')


if __name__ == '__main__':
    print(__package__)
    if sys.argv[1] == "delete" or  sys.argv[1] == "d":
        Generation.objects.all().delete()
        Type.objects.all().delete()
        Stat.objects.all().delete()
        Sprite.objects.all().delete()
        Pokemon.objects.all().delete()
    elif sys.argv[1] == "scrape" or sys.argv[1] == "s":
        scrape()
    elif sys.argv[1] == "type" or sys.argv[1] == "type":
        Type.objects.all().delete()
        type_scrape()
    else:
        scrape()