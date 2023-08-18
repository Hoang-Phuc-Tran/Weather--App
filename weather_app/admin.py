from django.contrib import admin
from .models import City
# Register your models here.
class CityApp(admin.ModelAdmin):
    list_display = ('name', 'updated_at')
    search_fields = ('name',)

admin.site.register(City,CityApp)