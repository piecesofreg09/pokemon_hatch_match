from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname')

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('name', 'hp', 'attack', 'defense', 
        'special_attack', 'special_defense', 'speed')

@admin.register(Sprite)
class SpriteAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('idd', 'name', 'cost', 'generation', 'user_defined')
    list_filter = ('generation', 'user_defined')

class PokemonInline(admin.TabularInline):
    model = Pokemon
    extra = 0

@admin.register(Generation)
class GenerationAdmin(admin.ModelAdmin):
    list_display = ('generation_number', )
    inlines = [PokemonInline]


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('type_number', 'name')
    
    
