from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from job.views import AboutView, IndexView, VacanciesView, \
    CompaniesView, CompanyView, VacancyView, ApplicationSentView,\
    MyCompanyView, MyCompanyVacanciesView, MyCompanyVacancyEditView, \
    MyLoginView, LogoutView, MySignupView


urlpatterns = [
    path('', IndexView.as_view()),
    path('about', AboutView.as_view()),
    path('login', MyLoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('register', MySignupView.as_view()),
    path('mycompany', MyCompanyView.as_view()),
    path('mycompany/vacancies', MyCompanyVacanciesView.as_view()),
    path('mycompany/vacancies/<int:vacancy_id>',
         MyCompanyVacancyEditView.as_view()),
    path('vacancies', VacanciesView.as_view()),
    path('vacancies/cat/<str:vacancy_category>', VacanciesView.as_view()),
    path('vacancies/<int:vacancy_id>', VacancyView.as_view()),
    path('vacancies/<int:vacancy_id>/sent', ApplicationSentView.as_view()),
    path('companies', CompaniesView.as_view()),
    path('companies/<int:company_id>', CompanyView.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
