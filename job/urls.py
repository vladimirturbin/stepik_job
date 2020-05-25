from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from job.views import AboutView, IndexView, VacanciesView, \
    CompaniesView, CompanyView, VacancyView


urlpatterns = [
    path('', IndexView.as_view()),
    path('about', AboutView.as_view()),
    path('vacancies', VacanciesView.as_view()),
    path('vacancies/cat/<str:vacancy_category>', VacanciesView.as_view()),
    path('companies', CompaniesView.as_view()),
    path('companies/<int:company_id>', CompanyView.as_view()),
    path('vacancies/<int:vacancy_id>', VacancyView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
