from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=128, unique=True,
                            verbose_name='Название компании')
    location = models.CharField(max_length=128, blank=True,
                                verbose_name='Город')
    logo = models.CharField(max_length=128,
                            blank=True,
                            verbose_name='Логотипчик')
    description = models.TextField(blank=True,
                                   verbose_name='Информация о компании')
    employee_count = models.IntegerField(
        verbose_name='Количество сотрудников'
    )


class Speciality(models.Model):
    code = models.CharField(max_length=32, verbose_name='Код')
    title = models.CharField(max_length=128, verbose_name='Название вакансии')
    picture = models.CharField(max_length=128,
                               blank=True,
                               verbose_name='Картинка')


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
    skills = models.TextField(verbose_name='Навыки'),
    text = models.TextField(verbose_name='Текст вакансии')
    salary_min = models.IntegerField(verbose_name='Зарплата от')
    salary_max = models.IntegerField(verbose_name='Зарплата до')
    published_at = models.DateTimeField(verbose_name='Опубликовано')
