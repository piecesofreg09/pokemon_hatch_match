from django.shortcuts import render
from django.urls import reverse
import requests, json
from django.core import serializers

# Create your views here.

def HatchIndex(request):
    result = requests.get(request.scheme + "://" + request.get_host() + reverse('poke-api-pokemons')).text
    result_json = json.loads(result)
    result_json_to_text = [{'id': i['id'], 'text': i['name']} for i in result_json]
    #print(result_json)
    context = {
        'pokemon_list': result_json_to_text, 
        'pokemons_s2_url': reverse('poke-api-pokemons-select2'),
        'sprite_url': reverse('poke-api-sprites', kwargs={'pid':100001, 'option': 100002})
    }
    
    return render(request, 'hatch.html', context=context)