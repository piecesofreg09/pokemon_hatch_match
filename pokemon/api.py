from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse

from django.urls import reverse_lazy

import datetime

from .models import *

def PokemonsAPIJson(request):
    poke_objects = Pokemon.objects.all()
    data = [{'id':i.idd, 'name': i.name} for i in poke_objects]
    print(len(data))
    return JsonResponse(data=data, safe=False)

def PokemonsAPIJsonSelect2(request):
    poke_objects = Pokemon.objects.all()
    data = {"results":[{'id':i.idd, 'text': i.name} for i in poke_objects]}
    print(len(data))
    return JsonResponse(data=data)

def SpriteAPIJson(request, pid, option):
    if option == 0:
        sprite_url = Pokemon.objects.all().get(pk=pid).sprites.front_default
    elif option == 1:
        sprite_url = Pokemon.objects.all().get(pk=pid).sprites.back_default
    elif option == 2:
        sprite_url = Pokemon.objects.all().get(pk=pid).sprites.svg_sprite
    elif option == 3:
        sprite_url = Pokemon.objects.all().get(pk=pid).sprites.big_sprite
    else:
        sprite_url = ''
    print(sprite_url)
    
    return JsonResponse(data=sprite_url, safe=False)