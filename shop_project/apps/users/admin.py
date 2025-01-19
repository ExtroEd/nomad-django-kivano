from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'username', 'email', 'first_name', 'last_name',
                    'is_staff', 'is_active', 'phone', 'address', 'middle_name',
                    'newsletter_subscription')
    list_filter = ('is_staff', 'is_active', 'groups')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone',
                     'middle_name')
    ordering = ('username',)

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'address',
                       'middle_name')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Subscription', {
            'fields': ('newsletter_subscription',)
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name',
                       'last_name', 'email', 'phone', 'address', 'middle_name',
                       'newsletter_subscription', 'is_active', 'is_staff')
        }),
    )

    readonly_fields = ('last_login', 'date_joined')

    verbose_name = "Регистрация пользователя"
    verbose_name_plural = "Регистрация пользователей"

admin.site.register(CustomUser, CustomUserAdmin)
