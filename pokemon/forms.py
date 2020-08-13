from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

class SignUpProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('nickname',)

class UpdateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('password1', 'password2', )

class UpdateProfileForm(UserCreationForm):

    class Meta:
        model = Profile
        fields = ('nickname',)