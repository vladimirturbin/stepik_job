# from datetime import datetime
# from django.core.management.base import BaseCommand
# from data import companies, specialties, jobs
# from job.models import Company, Speciality, Vacancy
#
#
# class Command(BaseCommand):
#     help = 'Import data from data.py'
#
#     def handle(self, *args, **options):
#         for i in Vacancy.objects.all():
#             i.skills = 'IDE • debug • GIT • coding • docker'
#             i.save()
#
# #         # for i in companies:
# #         #     Company.objects.create(name=i['title'], employee_count=0)
# #
# #         # for i in Company.objects.all():
# #         #     print(i.id, i.name,i.logo)
# #         #     i.logo = f'job/logo{i.id}.png'
# #         #     i.save()
# #
# #
# #         # for i in specialties:
# #         #     Speciality.objects.create(code=i['code'], title=i['title'])
# #
# #         # for i in Speciality.objects.all():
# #         #
# #         #     i.picture = f'job/specty_{i.code}.png'
# #         #     i.save()
# #         #     print(i.id, i.code, i.title, i.picture)
# #
# #
# #         # for i in jobs:
# #         #
# #         #     Vacancy.objects.create(
# #         #         title=i['title'],
# #         #         specialty=Speciality.objects.get(code=i['cat']),
# #         #         company=Company.objects.get(name=i['company']),
# #         #         text=i['desc'],
# #         #         salary_min=int(i['salary_from']),
# #         #         salary_max=int(i['salary_to']),
# #         #         published_at=datetime.strptime(i['posted'],
# #         '%Y-%m-%d').date()
# #         #     )
# #         # Vacancy.objects.all().update(skills='123')
# #
#
