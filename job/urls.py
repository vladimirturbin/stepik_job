from django.urls import path, include
from job.views import IndexView, AllVacanciesView,\
    VacanciesByCategoryView, CompanyView, VacancyView


urlpatterns = [
    path('', IndexView.as_view()),
    path('vacancies', AllVacanciesView.as_view()),
    path('vacancies/cat/<str:vacancy_category>',
         VacanciesByCategoryView.as_view()),
    path('companies/<int:company_id>', CompanyView.as_view()),
    path('vacancies/<int:vacancy_id>', VacancyView.as_view()),
]