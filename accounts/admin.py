from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomeUserChangeForm , CustomeUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomeUserCreationForm
    form = CustomeUserChangeForm
    model = CustomUser
    list_display = [
        'first_name',
        'last_name',
        'username',
        'acsses',
        'is_staff'
    ]
    add_fieldsets = UserAdmin.fieldsets + (
            (None, {
                'fields': (
                    'picture',
                    'acsses',
                ),
            }),
        )
    fieldsets = UserAdmin.add_fieldsets + (
            (None, {
                'fields': (
                    'picture',
                    'acsses',
                ),
            }),
        )

admin.site.register(CustomUser,CustomUserAdmin)