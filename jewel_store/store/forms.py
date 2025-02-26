from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.forms import widgets
from django.utils.translation import gettext, gettext_lazy as _
from store.models import Address

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        labels={'email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'})}
        

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class AddressForm(forms.ModelForm):
    class Meta:
        model=Address
        fields=['locality','city','state']
        widgets={'locality':forms.TextInput(attrs={'class':'form-control','placeholder':'Popular Place'}),'city':forms.TextInput(attrs={'class':'form-control','placeholder':'city'}),'state':forms.TextInput(attrs={'class':'form-control','placeholder':'State'})}
        