from django.contrib import admin
from .models import armorySearch

class PythonArmoryAdmin (admin.ModelAdmin):
    list_display = ('charName', 'armoryDate')

admin.site.register(armorySearch, PythonArmoryAdmin)

# Register your models here.