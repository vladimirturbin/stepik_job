from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {}

        return HttpResponse('Here will be index')
        # return render(request, 'index.html', context)


class AllVacanciesView(View):
    def get(self, request, *args, **kwargs):
        context = {}

        return HttpResponse('Here will be all vacancies')
        # return render(request, 'index.html', context)


class VacanciesByCategoryView(View):
    def get(self, request, *args, **kwargs):
        context = {}

        return HttpResponse('Here will be vacancies for category '
                            + kwargs['vacancy_category'])
        # return render(request, 'index.html', context)


class CompanyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Here will be info about company id '
                            + str(kwargs['company_id']))


class VacancyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Here will be info about vacancy id '
                            + str(kwargs['vacancy_id']))
