from django.shortcuts import render
from django.urls import reverse
import requests, json
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import SubmitTwoPokemonsForm

# Create your views here.

def HatchIndex(request):
    if request.method=="POST":
        print(request.POST.items())
        for k, v in request.POST.items():
            print(str(k) + '  ' + str(v))
        form = SubmitTwoPokemonsForm(request.POST)
        #print(form)
        #print(form.cleaned_data)
        if form.is_valid():
            #print("in form valid")
            print(form.cleaned_data)
            context={
                'data': form.cleaned_data,
                'sprite_url': reverse('poke-api-sprites', kwargs={'pid':100001, 'option': 100002}),
                'stat_url': reverse('poke-api-pokemon-ind-stat', kwargs={'pk':100001}),
            }
            return render(request, 'hatch.html', context=context)
    else:
        form = SubmitTwoPokemonsForm(initial={'pokemon_1': 0, 'pokemon_2': 0})
    
    # prepare general data for select 2
    result = requests.get(request.scheme + "://" + request.get_host() + reverse('poke-api-pokemons')).text
    result_json = json.loads(result)
    result_json_to_text = {"results": [{"id": i['id'], "text": str(i['id']) + ' - ' + str(i['name'])} for i in result_json]}
    
    #print(result_json)
    context = {
        'pokemon_list': result_json_to_text, 
        'pokemons_s2_url': reverse('poke-api-pokemons-select2'),
        'sprite_url': reverse('poke-api-sprites', kwargs={'pid':100001, 'option': 100002}),
        'stat_url': reverse('poke-api-pokemon-ind-stat', kwargs={'pk':100001}),
        'form': form,
        'post_url': reverse('hatch-submit')
    }
    
    return render(request, 'hatch_select.html', context=context)

def HatchPostHatchPairView(request):
    if request.method=="POST":
        print(request.POST.items())
    else:
        pass
    return

def HatchedListView(request):
    return