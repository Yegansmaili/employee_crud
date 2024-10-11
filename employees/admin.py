from django.contrib import admin

from .models import *


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user','first_name', 'last_name','position', 'salary', 'start_date', 'is_employed', 'phone_number',
                    'email', ]
