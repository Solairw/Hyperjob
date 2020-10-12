from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.views import View
# from django.contrib.auth import get_user_model
from .models import Vacancy
from django import forms
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


class Vacancies(View):
    def get(self, request, *args, **kwargs):
        vacancies_list = Vacancy.objects.all()
        return render(request, 'vacancy/vacancies.html', {'vacancies': vacancies_list})


class VacancyForm(forms.Form):
    description = forms.CharField(max_length=100)


class CreateVacancy(View):
    def get(self, request, *args, **kwargs):
        form = VacancyForm()
        return render(request, 'vacancy/new.html', {'form': form})

    def post(self, request):
        if request.user.is_staff:
            if request.method == 'POST':
                form = VacancyForm(request.POST)
                if form.is_valid():
                    return redirect('/home')
        return HttpResponseForbidden('You are mot allowed to post vacancies')
