from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from job.models import Company, Vacancy, Speciality


class IndexView(View):
    def get(self, request, *args, **kwargs):

        # Карточек (копаний или специальностей) в ряд на главной:
        cards_in_row = 4
        # Здесь можно отключить вывод тех карточек, у которых 0 вакансий:
        show_empty_cards = True

        context = {'title': 'Главная'}

        vacancies_all = list()
        vacancies_row = list()
        for i in Speciality.objects.all():
            if show_empty_cards or i.vacancies.count() != 0:
                vacancy = {
                    'picture': i.picture,
                    'name': i.title,
                    'code': i.code,
                    'count': i.vacancy_counter_for_href()
                }
                if len(vacancies_row) < cards_in_row:
                    vacancies_row.append(vacancy)
                else:
                    vacancies_all.append(vacancies_row)
                    vacancies_row = list()
                    vacancies_row.append(vacancy)
        if len(vacancies_row) > 0:
            vacancies_all.append(vacancies_row)
        context['vacancies'] = vacancies_all

        # Вот здесь можно было бы обойтись без копипасты, наверное. Если
        # бы мы изначально назвали поля таблиц одинаково? А без этого не
        # придумал, как объединить...

        companies_all = list()
        companies_row = list()
        for i in Company.objects.all():
            if show_empty_cards or i.vacancies.count() != 0:
                company = {
                    'logo': i.logo,
                    'name': i.name,
                    'id': i.id,
                    'count': i.vacancy_counter_for_href()
                }
                if len(companies_row) < cards_in_row:
                    companies_row.append(company)
                else:
                    companies_all.append(companies_row)
                    companies_row = list()
                    companies_row.append(company)
        if len(companies_row) > 0:
            companies_all.append(companies_row)
        context['companies'] = companies_all

        return render(request, 'index.html', context)


class AboutView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'О проекте',
            'text': 'Учебный проект курса stepic по Django'

        }
        return render(request, 'about.html', context)


class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        # Опция, показывать ли категории без вакансий на странице вакансий
        show_empty_specialities = True

        try:
            kwargs['vacancy_category']
        except KeyError:
            src = Speciality.objects.all()
        else:
            try:
                src = \
                    [Speciality.objects.get(code=kwargs['vacancy_category'])]
            except Speciality.DoesNotExist:
                raise Http404
        # TODO: вместо
        #         try:
        #             kwargs['vacancy_category']
        #         except KeyError
        #  сделать класс-наследник, который
        #         будет вызываться без vacancy_category и вызывать этот

        context = {'title': 'Вакансии',
                   'specialities': src,
                   'show_empty_specialities': show_empty_specialities,}

        return render(request, 'vacancies.html', context)


class CompanyView(View):
    def get(self, request, company_id, *args, **kwargs):
        company = get_object_or_404(Company, id=company_id)
        context = {
                   'title': 'Компания ' + company.name,
                   'back': request.META['HTTP_REFERER'],
                   'company': company,
                   'jobs': company.vacancies.all()}

        return render(request, 'company.html', context)


class CompaniesView(View):
    def get(self, request, *args, **kwargs):
        context = {'title': 'Компании', 'companies': Company.objects.all()}
        return render(request, 'companies.html', context)


class VacancyView(View):
    def get(self, request, vacancy_id, *args, **kwargs):
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)
        context = {'vacancy': vacancy,
                   # 'back': request.META['HTTP_REFERER']
                   }
        # TODO: fix bug with null HTTP_REFERER after direct URL address input
        return render(request, 'vacancy.html', context)


class ApplicationSentView(View):
    def get(self, request, *args, **kwargs):

        context = {}

        return render(request, 'sent.html', context)


class MyCompanyView(View):
    def get(self, request, *args, **kwargs):

        context = {}

        return render(request, 'mycompany.html', context)


class MyCompanyVacanciesView(View):
    def get(self, request, *args, **kwargs):

        context = {}

        return render(request, 'mycompany-vacancies.html', context)


class MyCompanyVacancyEditView(View):
    def get(self, request, vacancy_id, *args, **kwargs):

        context = {}

        return render(request, 'mycompany-vacancy-edit.html', context)


class LoginView(View):
    def get(self, request, *args, **kwargs):

        context = {}

        return render(request, 'login.html', context)


class RegisterView(View):
    def get(self, request, *args, **kwargs):

        context = {}

        return render(request, 'register.html', context)


class LogoutView(View):
    def get(self, request, *args, **kwargs):

        context = {}

        return redirect('/')
