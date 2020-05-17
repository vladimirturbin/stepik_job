from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Главная'
        }

        # return HttpResponse('Here will be index')
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