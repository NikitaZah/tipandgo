from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import CustomUserChangeForm, CustomUserCreationForm

admin.site.register(User)
admin.site.register(Staff)
admin.site.register(Institution)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Address)
admin.site.register(Position)
admin.site.register(InstitutionType)
admin.site.register(Currency)
admin.site.register(Client)
admin.site.register(Tips)
admin.site.register(Applicant)
admin.site.register(PreRegisteredUser)
admin.site.register(Review)


class Admin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'first_name', 'last_name',  'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
