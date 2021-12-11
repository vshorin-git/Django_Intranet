from django.contrib import admin
from .models import Employee, Company, Role, City, MailingGroup


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'manager', 'city')
    list_filter = ('manager', 'city', 'mailing_groups')
    fieldsets = (
        ('Personal info', {'fields':(('first_name', 'last_name'), ('sex', 'birth_date', 'photo'), ('phone', 'email'), 'city')}),
        ('Role in the company', {'fields':('role', 'start_date', 'manager', 'mailing_groups')}),
        ('Additional info', {'fields':('description',)})
    )


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Role)
admin.site.register(City)
admin.site.register(MailingGroup)