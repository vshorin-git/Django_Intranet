from django.contrib import admin
from .models import Employee, Company, Role, City
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'manager', 'city')
    list_filter = ('manager', 'city')
    fieldsets = (
        ('Personal info', {'fields':(('user','first_name', 'last_name'), ('sex', 'birth_date', 'photo'), ('phone', 'email'), 'city')}),
        ('Role in the company', {'fields':('role', 'start_date', 'manager', 'mailing_groups')}),
        ('Additional info', {'fields':('description',)})
    )

class EmployeeAdminInLine(admin.StackedInline):
    model = Employee


    def queryset(self, request):
        qs = super(EmployeeAdmin, self).queryset(request)
        qs = qs.exclude(relatedNameForYourProduct__isnone=True)
        return qs


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

class UserAdmin(AuthUserAdmin):
    inlines = [EmployeeAdminInLine]

admin.site.register(Employee, EmployeeAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.register(City)