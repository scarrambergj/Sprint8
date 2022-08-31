from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  
        (                     
            'Cliente',  
            {
                'fields': (
                    'cliente',
                    'empleado',
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
