from django.contrib import admin
from DentCorpApp.models import User
from django.contrib.auth.admin import UserAdmin

class UserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'image', )
    
admin.site.register(User, UserAdmin)