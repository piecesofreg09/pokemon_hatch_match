from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('pokemons/', views.PokemonListView.as_view(), name='pokemons'),
    path('pokemons/<int:pk>', views.PokemonDetailView.as_view(), name='pokemon-detail'),
    path('generations/', views.GenerationListView.as_view(), name='generations'),
    path('generations/<int:pk>', views.GenerationDetailView.as_view(), name='generation-detail'),
    path('types/', views.TypeListView.as_view(), name='types'),
    path('types/<int:pk>', views.TypeDetailView.as_view(), name='type-detail'),
    # a path for testing purposes
    path('test/<int:pp>/<int:xx>', views.Test, name='test'),
]