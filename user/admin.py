from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from user.models import Administrator


@admin.register(get_user_model())
class UserAdmin(DjangoUserAdmin):
    ordering = ('date_joined',)
    search_fields = [
        'first_name',
        'last_name',
        'email',
    ]
    list_display = [
        'fio',
        'email',
    ]
    list_filter = ()

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
            'first_name', 'last_name')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    def fio(self, obj):
        return obj.name

    fio.short_description = "ФИО"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_staff=False)


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):

    list_display = (
        'email',
        'first_name',
        'last_name',
    )
    search_fields = fields = list_display

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        return qs.filter(is_staff=True)

    def save_model(self, request, obj, form, change):
        obj.is_staff = True
        obj.is_superuser = True
        super().save_model(request, obj, form, change)
