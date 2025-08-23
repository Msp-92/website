from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomeUserCreationForm, CustomeUserChangeForm

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

    # برای اضافه کردن کاربر جدید
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('picture', 'acsses'),
        }),
    )

    # برای ویرایش کاربر موجود
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('picture', 'acsses'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
