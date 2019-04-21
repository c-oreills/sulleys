from django.contrib import admin
from buildings.models import Building

class BuildingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Building, BuildingAdmin)
