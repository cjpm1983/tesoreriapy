from django import forms
from encuestas.models import UserProfile
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserProfileForm(UserCreationForm):
    class Meta:
        model = UserProfile
        #fields = ['username','email','password1','password2','first_name','last_name','avatar', 'background' ]
        #fields = ['username', 'email', 'password', 'first_name', 'last_name', 'avatar', 'background']
        fields = [ 'email', 'first_name', 'last_name', 'avatar', 'background']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-alternative'}),
            #'password1': forms.PasswordInput(attrs={'class': 'form-control form-control-alternative'}),
            #'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-alternative', 'placeholder':'Repeat Password'}),
            #'password': forms.PasswordInput(attrs={'class': 'form-control form-control-alternative', 'placeholder':'Repeat Password'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-alternative'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-alternative'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-alternative'})
        }
        #localized_fields = '__all__'

class UserProfileCreationForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileChangeForm(UserChangeForm):
    class Meta:
        model = UserProfile
        #fields = ('username', )
        fields = ('username','email','password','first_name','last_name','avatar', 'background')
        #widgets = {
            #'avatar': forms.ImageField(),
            #'background': forms.ImageField()
        #}