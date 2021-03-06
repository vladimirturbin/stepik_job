# Generated by Django 3.0.6 on 2020-05-17 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Название компании')),
                ('location', models.CharField(blank=True, max_length=128, verbose_name='Город')),
                ('logo', models.CharField(blank=True, max_length=128, verbose_name='Логотипчик')),
                ('description', models.TextField(blank=True, verbose_name='Информация о компании')),
                ('employee_count', models.IntegerField(verbose_name='Количество сотрудников')),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32, verbose_name='Код')),
                ('title', models.CharField(max_length=128, verbose_name='Название вакансии')),
                ('picture', models.CharField(blank=True, max_length=128, verbose_name='Картинка')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название вакансии')),
                ('text', models.TextField(verbose_name='Текст вакансии')),
                ('salary_min', models.IntegerField(verbose_name='Зарплата от')),
                ('salary_max', models.IntegerField(verbose_name='Зарплата до')),
                ('published_at', models.DateTimeField(verbose_name='Опубликовано')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='job.Company', verbose_name='Компания')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='job.Speciality', verbose_name='Специализация')),
            ],
        ),
    ]
