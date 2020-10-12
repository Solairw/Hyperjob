from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.db import models

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


class MainPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'hyperjob/index.html')


class LoginPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'hyperjob/login.html')


class SignupPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'hyperjob/signup.html')


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'


class HomePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'hyperjob/home.html')


class ResumeForm(models.Model):
    description = models.CharField(max_length=100)


class VacancyForm(models.Model):
    description = models.CharField(max_length=100)
