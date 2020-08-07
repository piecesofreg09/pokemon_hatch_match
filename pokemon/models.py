from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Generation(models.Model):
    """Model representing the generation number, such as 1, 2, 3, ..."""
    generation_number = models.IntegerField(primary_key=True, 
        help_text='the official generation number')

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return str(self.generation_number)
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('generation-detail', args=[str(self.generation_number)])


class Type(models.Model):
    """Model representing the type, such as grass, poison, ..."""
    type_number = models.IntegerField(primary_key=True, 
        help_text='type number')
    name = models.CharField(max_length=30,
                            help_text="the type of the selected pokemon")
    double_damage_from = models.ManyToManyField('self', symmetrical=False,
        related_name='double_damage_from_set', blank=True)
    double_damage_to = models.ManyToManyField('self', symmetrical=False,
        related_name='double_damage_to_set', blank=True)
    half_damage_from = models.ManyToManyField('self', symmetrical=False,
        related_name='half_damage_from_set', blank=True)
    half_damage_to = models.ManyToManyField('self', symmetrical=False,
        related_name='half_damage_to_set', blank=True)
    no_damage_from = models.ManyToManyField('self', symmetrical=False,
        related_name='no_damage_from_set', blank=True)
    no_damage_to = models.ManyToManyField('self', symmetrical=False,
        related_name='no_damage_to_set', blank=True)

    sprite_url = models.URLField(help_text='the url of the sprite of the required type')

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('type-detail', args=[str(self.type_number)])

class Relationship(models.Model):
    from_pokemon = models.ForeignKey(Type, related_name='from_pokemon', 
        on_delete=models.CASCADE)
    to_pokemon = models.ForeignKey(Type, related_name='to_pokemon', 
        on_delete=models.CASCADE)

class Stat(models.Model):
    """Stat object, including six stats:
    hp, attack, defense, special-attack, special-defense, speed"""

    name = models.CharField(max_length=30, 
        help_text='name of the pokemon this set of stats belongs to')

    hp = models.IntegerField(help_text='Hit point (health point)')
    attack = models.IntegerField(help_text='Attack point')
    defense = models.IntegerField(help_text='Ability to defend, mapped to a ratio')
    special_attack = models.IntegerField(help_text='Special attack point')
    special_attack_acc_rounds = models.IntegerField(help_text='Rounds to trigger special attack')
    special_defense = models.IntegerField(help_text='Special defense point')
    speed = models.IntegerField(help_text='Speed')

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return f'{self.hp}, {self.attack}, {self.defense}'
    
    def special_defense_probability(self):
        return self.special_defense / 200

class Sprite(models.Model):
    """
    Sprites links for a specific pokemon.
    First three links are from pokemon api, big_sprite is from bulbapedia.
    """
    name = models.CharField(max_length=30,
        help_text='name of the pokemon this set of sprites belongs to')
    back_default = models.URLField(max_length=300, verbose_name='default back url')
    front_default = models.URLField(max_length=300, verbose_name='default back url')
    svg_sprite = models.URLField(max_length=300, verbose_name='default back url')

    big_sprite = models.URLField(max_length=300, verbose_name='default back url')
    
    def __str__(self):
        return 'Sprites object'

# Create your models here.
class Pokemon(models.Model):
    """Model representing a pokemon."""
    idd = models.IntegerField(primary_key=True, help_text='Pokemon id in the official game')
    name = models.CharField(max_length=30, help_text='Name of the pokemon')

    weight = models.IntegerField()
    height = models.IntegerField()
    base_exp = models.IntegerField()
    cost = models.IntegerField(default=45)

    stat = models.OneToOneField(Stat, on_delete=models.CASCADE)
    sprites = models.OneToOneField(Sprite, on_delete=models.CASCADE)
    generation = models.ForeignKey(Generation, on_delete=models.CASCADE)
    types = models.ManyToManyField(Type)

    user_defined = models.BooleanField()
    

    class Meta:
        ordering = ['idd']

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('pokemon-detail', args=[str(self.idd)])
