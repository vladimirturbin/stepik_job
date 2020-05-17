from django.http import HttpResponse
from django.shortcuts import render
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
            'title': 'О проекте'
        }

        # return HttpResponse('Here will be index')
        return render(request, 'about.html', context)


class AllVacanciesView(View):
    def get(self, request, *args, **kwargs):
        context = {'title': 'Вакансии'}

        # return HttpResponse('Here will be all vacancies')
        return render(request, 'vacancies.html', context)


class VacanciesByCategoryView(View):
    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, 'vacancies.html', context)


class CompanyView(View):
    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, 'company.html', context)


class CompaniesView(View):
    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, 'companies.html', context)


class VacancyView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'vacancy.html')