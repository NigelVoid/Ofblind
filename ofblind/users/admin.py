from django.contrib import admin
from .models import CustomUser, ApplicantProfile, EmployerProfile
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'status', 'is_staff')
    list_filter = ('status', 'is_staff')

@admin.register(ApplicantProfile)
class ApplicantProfileAdmin(admin.ModelAdmin):
    # Колоночки, которые будут видны в списке в админке
    list_display = ('user', 'github_username', 'skills')
    # Возможность искать профили по имени пользователя или гитхабу
    search_fields = ('user__username', 'github_username', 'skills')
@admin.register(EmployerProfile)
class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)
