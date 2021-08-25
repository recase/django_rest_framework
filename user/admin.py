from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserChangeForm, CustomUserCreateionForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateionForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'first_name', 'last_name',
                    'is_active', 'is_staff')
    list_filter = ('email', 'first_name', 'last_name', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name')}),
        ('permissions', {'fields': ('is_staff',
         'is_active', 'groups', 'user_permissions')})
    )
    add_fieldsets = (
        (None, {
            'classes': 'wide',
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff', 'groups', 'user_permissions')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
