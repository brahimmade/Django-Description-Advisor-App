from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from .forms import RegisterForm,AuthenticationForm,CustomPasswordResetForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import views

User = get_user_model()

class RegisterView(SuccessMessageMixin,CreateView):
    template_name = "registration/registration.html"
    queryset = User.objects.all()
    models = User
    form_class  = RegisterForm
    success_message = "your account has been created successfully, please login and continue registration"
    success_url = reverse_lazy("accounts:login")

class LoginView(views.LoginView):
    form_class = AuthenticationForm    

class PasswordResetView(views.PasswordResetView):
    form_class = CustomPasswordResetForm