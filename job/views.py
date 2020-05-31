from django.contrib.auth import get_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View

from job.models import Company, Vacancy, Speciality
from job.forms import RegisterForm


class IndexView(View):
    def get(self, request, *args, **kwargs):

        # Карточек (копаний или специальностей) в ряд на главной:
        cards_in_row = 4
        # Здесь можно отключить вывод тех карточек, у которых 0 вакансий:
        show_empty_cards = True

        user = get_user(request)
        context = {'title': 'Главная',
                   'user': user}
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
        user = get_user(request)
        context = {
            'title': 'О проекте',
            'text': 'Учебный проект курса stepic по Django',
            'user': user}


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
        user = get_user(request)

        context = {'title': 'Вакансии',
                   'specialities': src,
                   'show_empty_specialities': show_empty_specialities,
                   'user': user,}

        return render(request, 'vacancies.html', context)


class CompanyView(View):
    def get(self, request, company_id, *args, **kwargs):
        company = get_object_or_404(Company, id=company_id)
        user = get_user(request)

        context = {
                   'title': 'Компания ' + company.name,
                   'back': request.META['HTTP_REFERER'],
                   'company': company,
                   'jobs': company.vacancies.all(),
                   'user': user,}
        # TODO: fix bug with null HTTP_REFERER after direct URL address input2
        return render(request, 'company.html', context)


class CompaniesView(View):
    def get(self, request, *args, **kwargs):
        user = get_user(request)
        context = {'title': 'Компании',
                   'companies': Company.objects.all(),
                   'user': user}
        return render(request, 'companies.html', context)


class VacancyView(View):
    def get(self, request, vacancy_id, *args, **kwargs):
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)
        user = get_user(request)
        context = {'vacancy': vacancy,
                   'user': user,
                   'back': request.META['HTTP_REFERER']
                   }
        # TODO: fix bug with null HTTP_REFERER after direct URL address input
        return render(request, 'vacancy.html', context)


class ApplicationSentView(View):
    def get(self, request, *args, **kwargs):
        user = get_user(request)
        context = {'title': 'Отклик отправлен', 'user': user}

        return render(request, 'sent.html', context)


class MyCompanyView(View):
    def get(self, request, *args, **kwargs):
        user = get_user(request)
        context = {'title': 'моя компания', 'user': user}

        return render(request, 'mycompany.html', context)


class MyCompanyVacanciesView(View):
    def get(self, request, *args, **kwargs):
        user = get_user(request)
        context = {'title': 'Вакансии моей компании', 'user': user}

        return render(request, 'mycompany-vacancies.html', context)


class MyCompanyVacancyEditView(View):
    def get(self, request, vacancy_id, *args, **kwargs):
        user = get_user(request)
        context = {'title': 'Редактирование вакансии', 'user': user}

        return render(request, 'mycompany-vacancy-edit.html', context)


class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()

        return render(request, 'register.html', {'form': form})

    def post(self, request, *args, **kwargs):

        form = RegisterForm(request.POST)

        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['email']):
                form.add_error('email',
                               'Пользователь с таким email уже существует')
            else:
                User.objects.create(
                    username=form.cleaned_data['email'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                )

                return redirect('/login')

        return render(request, 'register.html', {'form': form})


class MyLogoutView(LogoutView):

    pass
