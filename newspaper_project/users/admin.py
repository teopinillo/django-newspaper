from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin (UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

admin.site.register (CustomUser, CustomUserAdmin)

#need to:
#python manage.py makenigrations users
#python manage.py migrate
