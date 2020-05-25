from django.contrib.auth.models import User
from django.db import models
from plural_ru import ru


class Company(models.Model):
    name = models.CharField(max_length=128, unique=True,
                            verbose_name='Название компании')
    location = models.CharField(max_length=128, blank=True,
                                verbose_name='Город')
    logo = models.ImageField(max_length=128,
                             blank=True,
                             verbose_name='Логотипчик')
    description = models.TextField(blank=True,
                                   verbose_name='Информация о компании')
    employee_count = models.IntegerField(
        verbose_name='Количество сотрудников'
    )
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='Company',
                              verbose_name='Владелец',
                              default=1)

    def vacancy_counter_for_href(self):
        t = self.vacancies.count()
        return str(t) + ' ' + ru(t, ('вакансия', 'вакансии', 'вакансий'))

    def get_absolute_url(self):
        return '/vacancies/' + str(self.id)


class Speciality(models.Model):
    code = models.CharField(max_length=32, verbose_name='Код', unique=True)
    title = models.CharField(max_length=128, verbose_name='Название вакансии')
    picture = models.ImageField(max_length=128,
                                blank=True,
                                verbose_name='Картинка')

    def vacancy_counter_for_href(self):
        t = self.vacancies.count()
        return str(t) + ' ' + ru(t, ('вакансия', 'вакансии', 'вакансий'))

    def get_absolute_url(self):
        return '/vacancies/cat/' + str(self.code)


class Vacancy(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название вакансии')
    specialty = models.ForeignKey(Speciality,
                                  on_delete=models.CASCADE,
                                  related_name='vacancies',
                                  verbose_name='Специализация')
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                related_name='vacancies',
                                verbose_name='Компания')
    skills = models.CharField(max_length=128,
                              verbose_name='Навыки',
                              blank=True)
    text = models.TextField(verbose_name='Текст вакансии')
    salary_min = models.IntegerField(verbose_name='Зарплата от')
    salary_max = models.IntegerField(verbose_name='Зарплата до')
    published_at = models.DateField(verbose_name='Опубликовано')

    def get_absolute_url(self):
        return '/vacancies/' + str(self.id)


class Application(models.Model):
    written_username = models.CharField(max_length=128, verbose_name='Имя')
    written_phone = models.CharField(max_length=128, verbose_name='Телефон')
    written_cover_letter = models.TextField(
        verbose_name='Сопроводительное письмо')
    vacancy = models.ForeignKey(Vacancy,
                                on_delete=models.CASCADE,
                                related_name='applications',
                                verbose_name='Вакансия')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='applications',
                             verbose_name='Пользователь')
