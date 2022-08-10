from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Cliente',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'cliente',
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
