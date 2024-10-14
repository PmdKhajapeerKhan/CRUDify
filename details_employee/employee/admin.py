from django.contrib import admin
from .models import Employee, EmployeeFinancialInfo

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'position')
    search_fields = ('first_name', 'last_name', 'email')
@admin.register(EmployeeFinancialInfo)
class EmployeeFinancialInfoAdmin(admin.ModelAdmin):
    list_display = ('salary', 'bank_details', 'account_number', 'ifsc_code', 'experience')
    search_fields = ('salary', 'bank_details', 'account_number', 'ifsc_code', 'experience')
