from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UserChangeForm, SetPasswordForm,PasswordResetForm
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
        fields = ['name','email','phone','company_name','refresh_token','zoho_domain','client_id','client_secret','cloudfare_email','cloudfare_auth_code','smart_lead_api_key']

    def __init__(self, *args, **kwargs):
        super(EditUserProfileForm, self).__init__(*args, **kwargs)

        # you can iterate all fields here
        for fname, f in self.fields.items():
            f.widget.attrs['class'] = 'border-[#2B2358] text-[#2B2358] border-2 mt-2 rounded-md w-[35rem] py-1.5 pl-6 font-medium text-base'    
    
class changePasswordForm(SetPasswordForm):
    class Meta:
        model = CustomUser
        fields = ['new_password1', 'new_password2']


class PasswordResetForm(PasswordResetForm):
    model = CustomUser
    fields = ['email']
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)