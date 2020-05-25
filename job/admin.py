from django.contrib import admin
from job.models import Company, Speciality


class CompanyAdmin(admin.ModelAdmin):
    pass


class SpecialityAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
admin.site.register(Speciality, SpecialityAdmin)
