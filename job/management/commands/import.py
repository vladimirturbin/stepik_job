from datetime import datetime
from django.core.management.base import BaseCommand
from data import companies, specialties, jobs
from job.models import Company, Speciality, Vacancy


class Command(BaseCommand):
    help = 'Import data from data.py'

    def handle(self, *args, **options):

        # for i in companies:
        #     Company.objects.create(name=i['title'], employee_count=0)

        # for i in specialties:
        #     Speciality.objects.create(code=i['code'], title=i['title'])
        # for i in Speciality.objects.all():
        #     print(i.id, i.code, i.title)

        # for i in jobs:
        #
        #     Vacancy.objects.create(
        #         title=i['title'],
        #         specialty=Speciality.objects.get(code=i['cat']),
        #         company=Company.objects.get(name=i['company']),
        #         text=i['desc'],
        #         salary_min=int(i['salary_from']),
        #         salary_max=int(i['salary_to']),
        #         published_at=datetime.strptime(i['posted'], '%Y-%m-%d').date()
        #     )

        for i in Vacancy.objects.all():
            print(i.id, i.title, i.text, i.company, i.specialty,
                  i.salary_max, i.salary_min, i.published_at)
