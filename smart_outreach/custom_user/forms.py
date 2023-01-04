from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UserChangeForm
from .models import CustomUser

class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ["email", "password1", "password2","name","company_name"]


class LoginForm(AuthenticationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ["email"]


class EditUserProfileForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ['name','email','phone','refresh_token','zoho_domain','client_id','client_secret','cloudfare_email','cloudfare_auth_code',]
    



