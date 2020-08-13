import sys, os, random
sys.path.append(os.path.abspath('..'))
from django.shortcuts import render
from django.urls import reverse
import requests, json
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import SubmitTwoPokemonsForm
from pokemon.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Max

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
                'post_url': reverse('hatch-submit'),
                'pokemon_url': reverse('poke-api-pokemon-ind', kwargs={'pk':100001}),
            }
            request.session['context'] = context
            return HttpResponseRedirect(reverse('hatch-prepare'))
            #return render(request, 'hatch.html', context=context)
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
    print(reverse('hatch-submit'))
    
    return render(request, 'hatch_select.html', context=context)

def HatchPrepareView(request):
    if request.user.is_authenticated:

        context = request.session['context']
        return render(request, 'hatch.html', context=context)
    else:
        return HttpResponseRedirect(reverse('hatch-index'))

def get_mix_poke_properties(poke1, poke2):
    pokemon_1 = Pokemon.objects.get(idd=int(poke1))
    pokemon_2 = Pokemon.objects.get(idd=int(poke2))
    weight = random.randint(pokemon_1.weight, pokemon_2.weight)
    return
    

@login_required
def HatchPostHatchPairView(request):
    if request.method=="POST":
        obj = {}
        for k, v in request.POST.items():
            #print(str(k)  + " " + str(v))
            obj[k] = v
        print(obj)

        
        user = request.user
        user_q = User.objects.get(id=user.id)
        profile_q = user_q.profile
        
        # create stat obj
        stat_created = Stat(name=obj['name'], attack=obj['attack'],
            defense=obj['defense'], hp=obj['hp'],
            special_attack=obj['special_attack'],
            special_attack_acc_rounds=obj['special_attack_acc_rounds'],
            special_defense=obj['special_defense'],
            speed=obj['speed']
        )
        stat_created.save()

        # create sprite obj
        sprite_created = Sprite(name=obj['name'])
        sprite_created.save()


        # create generation
        user_created_gen = 100
        gen_created = Generation(generation_number=user_created_gen)
        gen_created.save()

        # create pokemon
        max_id = int(Pokemon.objects.all().aggregate(Max('idd'))['idd__max'])
        print(max_id)
        boundry_value = 10000
        if max_id > boundry_value:
            idd_new = max_id + 1
        else:
            idd_new = boundry_value + 1
        pokemon_obj = Pokemon(idd=idd_new, name=obj['name'], height=obj['height'],
            weight=obj['weight'], base_exp=obj['base_exp'], cost=obj['cost'],
            user_defined=True, stat=stat_created, sprites=sprite_created,
            generation=gen_created)
        pokemon_obj.save()

        # find type and add types to pokemon
        types_01 = Pokemon.objects.get(pk=int(obj['pokemon_1'])).types
        types_02 = Pokemon.objects.get(pk=int(obj['pokemon_2'])).types
        type_1 = types_01.all()[random.randint(0, types_01.count() - 1)]
        type_2 = types_02.all()[random.randint(0, types_02.count() - 1)]
        pokemon_obj.types.add(type_1)
        pokemon_obj.types.add(type_2)

        # add pokemon to profile, save profile and user
        profile_q.pokemons_created.add(pokemon_obj)
        profile_q.save()
        user_q.save()

        print(user_q)
        print(profile_q)
        print(pokemon_obj)

        return HttpResponseRedirect(reverse('hatched-list'))
    # no get request for this view
    else:
        print('in get? Something is wrong')
        pass
    #return HttpResponseRedirect(reverse('hatched-index'))

@login_required
def HatchedListView(request):
    print(request.user)
    user = request.user
    user_q = User.objects.get(id=user.id)
    profile_q = user_q.profile
    all_hatched_pokemons = profile_q.pokemons_created.all()
    print(all_hatched_pokemons)
    context = {
        'all_hatched_pokemons': all_hatched_pokemons,

    }
    return render(request, 'hatch_list.html', context=context)