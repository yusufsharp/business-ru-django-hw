from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_surname', 'image', 'gender', 'birth_date', 'telegram', 'phone_number', 'about')
    list_filter = ('name_surname', 'birth_date')
    search_fields = ('name_surname', 'birth_date')
    list_display_links = ('id', 'name_surname')


admin.site.register(models.User, UserAdmin)

