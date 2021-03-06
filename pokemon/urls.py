from django.urls import path
from . import views, api, profile_view
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
]

urlpatterns += [
    path('api/pokemons', api.PokemonsAPIJson, name='poke-api-pokemons'),
    path('api/pokemons_s2', api.PokemonsAPIJsonSelect2, name='poke-api-pokemons-select2'),
    path('api/sprites/<int:pid>/<int:option>', api.SpriteAPIJson, name='poke-api-sprites'),
    path('api/pokemon/<int:pk>', api.PokemonAPIJson, name='poke-api-pokemon-ind'),
    path('api/pokemon/stat/<int:pk>', api.PokemonStatAPIJson, name='poke-api-pokemon-ind-stat'),
]

urlpatterns += [
    path('accounts/profile/', profile_view.ProfileView, name="profile"),
]

urlpatterns += [
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/update', views.update_profile, name='update'),
]

urlpatterns += [
    path('test/<int:pp>/<int:xx>', views.Test, name='test'),
    path('test/test', views.TestTest),
]