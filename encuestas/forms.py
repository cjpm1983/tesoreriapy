from django import forms
from encuestas.models import UserProfile
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'background']

class MyUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

