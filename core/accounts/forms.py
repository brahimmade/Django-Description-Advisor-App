from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as form
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from captcha.fields import CaptchaField

User = get_user_model()


class RegisterForm(form.UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control form-control-user', 'placeholder': 'Enter Email Address...'})
        self.fields['email'].label = "Email Address"
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control form-control-user', 'placeholder': 'Password'})
        self.fields['password1'].label = "Password"
        self.fields['password1'].help_text = ""
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control form-control-user', 'placeholder': 'Confirmation Password'})
        self.fields['password2'].label = "Confirmation Password"
        self.fields['password2'].help_text = ""


class AuthenticationForm(form.AuthenticationForm):
    captcha = CaptchaField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control form-control-user', 'placeholder': 'Enter Email Address...'})
        self.fields['username'].label = "Email Address"
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control form-control-user', 'placeholder': 'Password'})
        #self.fields['password'].label = ""
        self.fields['captcha'].label = ""



class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update(
            {'class': 'form-control form-control-user', 'placeholder': 'Old Password'})
        self.fields['new_password1'].widget.attrs.update(
            {'class': 'form-control form-control-user', 'placeholder': 'New Password'})
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control form-control-user', 'placeholder': 'New Password Confirmation'})


class CustomPasswordResetForm(PasswordResetForm):
    
    def __init__(self, *args, **kwargs):        
        super().__init__(*args, **kwargs)
        
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control form-control-user', 'placeholder': 'Enter Email Address...'})

