from django.contrib import admin
from .models import Vacancy


class AdminVacancy(admin.ModelAdmin):
    list_display = ['id', 'company', 'uuid', 'title', 'created_at',
                    'updated_at', 'enabled']

    class Meta:
        model = Vacancy


admin.site.register(Vacancy, AdminVacancy)
