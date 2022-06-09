from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

from user.forms import UserCreationForm, UserChangeForm
from user.models import User


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_active')

    add_form = UserCreationForm
    form = UserChangeForm

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


admin.site.register(User, UserAdmin)
