"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from . import views
#
#
# urlpatterns = [
#     # path('', MenuView.as_view()),
#     path('vacancies/', views.Vacancies.as_view(), name='vacancy list'),
#     path('vacancies2/', views.Vacancies.as_view(), name='vacancy list'),
# ]


from django.urls import path
from . import views


urlpatterns = [
    # path('', views.MainPage.as_view(), name='main menu'),
    path('/', views.Vacancies.as_view(), name='vacancy list'),
    path('/new', views.CreateVacancy.as_view(), name='create vacancy')
    # path('', include('resume.urls'))
    # path('/vacancies/', vacancy.views.VacancyView.as_view()),
]
