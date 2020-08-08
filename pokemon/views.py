from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse

from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

import datetime

from .models import *

# Create your views here.
def index(request):
    """View function for home page of site."""
    gen_count = Generation.objects.all().count()
    type_count = Type.objects.all().count()
    pokemon_count = Pokemon.objects.all().count()
    context = {
        'gen_count': gen_count,
        'type_count': type_count,
        'pokemon_count': pokemon_count
    }
    return render(request, 'index.html', context=context)



class PokemonListView(generic.ListView):
    model = Pokemon
    # your own name for the list as a template variable
    context_object_name = 'all_pokemon_list'
    # Get 5 books containing the title war
    #queryset = Book.objects.filter(title__icontains='war')[:5] 
    # Specify your own template name/location
    #template_name = 'books/my_arbitrary_template_name_list.html' 
    paginate_by = 25

class PokemonDetailView(generic.DetailView):
    model = Pokemon


class GenerationListView(generic.ListView):
    model = Generation
    
    context_object_name = 'all_generation_list'
    
    paginate_by = 10

class GenerationDetailView(generic.ListView):
    
    paginate_by  = 20
    template_name = 'pokemon/generation_detail.html'

    def get_queryset(self):
        return Generation.objects.get(pk=self.kwargs['pk']).pokemon_set.all()
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['generation'] = Generation.objects.get(pk=self.kwargs['pk'])
        
        return context

class TypeListView(generic.ListView):
    model = Type
    
    context_object_name = 'all_type_list'
    
    paginate_by = 10

class TypeDetailView(generic.ListView):
    
    paginate_by  = 20
    template_name = 'pokemon/type_detail.html'

    def get_queryset(self):
        return Type.objects.get(pk=self.kwargs['pk']).pokemon_set.all()
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['type'] = Type.objects.get(pk=self.kwargs['pk'])
        
        return context


def Test(request, pp, xx):
    context = {"var1": pp, "var2": xx}
    return render(request, 'test.html', context=context)

def TestTest(request):
    data = {1.5: 2}
    return JsonResponse(data)
