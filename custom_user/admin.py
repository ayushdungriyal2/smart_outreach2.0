from django.contrib import admin
from .models import CustomUser, tempUsers

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(tempUsers)