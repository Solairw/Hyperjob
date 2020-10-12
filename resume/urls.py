from django.urls import path
from . import views


urlpatterns = [
    # path('', views.MainPage.as_view(), name='main menu'),
    path('/', views.Resumes.as_view(), name='resume list'),
    path('/new', views.CreateResume.as_view(), name='create resume')
    # path('', include('resume.urls'))
    # path('/vacancies/', vacancy.views.VacancyView.as_view()),
]
