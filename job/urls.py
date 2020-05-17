from django.urls import path, include
from job.views import AboutView, IndexView, AllVacanciesView,\
    VacanciesByCategoryView, CompaniesView, CompanyView, VacancyView


urlpatterns = [
    path('', IndexView.as_view()),
    path('about', AboutView.as_view()),
    path('vacancies', AllVacanciesView.as_view()),
    path('vacancies/cat/<str:vacancy_category>',
         VacanciesByCategoryView.as_view()),
    path('companies', CompaniesView.as_view()),
    path('companies/<int:company_id>', CompanyView.as_view()),
    path('vacancies/<int:vacancy_id>', VacancyView.as_view()),
]