from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class SubmitTwoPokemonsForm(forms.Form):
    pokemon_1 = forms.IntegerField()
    pokemon_2 = forms.IntegerField()

    def clean_pokemon_1(self):
        data = self.cleaned_data['pokemon_1']
        
        if data < 1:
            raise ValidationError(_("You didn't choose Pokemon 1"))
        
        return data
    
    def clean_pokemon_2(self):
        data = self.cleaned_data['pokemon_2']
        
        if data < 1:
            raise ValidationError(_("You didn't choose Pokemon 2"))

       
        return data