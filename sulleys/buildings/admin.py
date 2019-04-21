from django.contrib import admin

from cms.admin.placeholderadmin import FrontendEditableAdminMixin

from buildings.models import Building

class BuildingAdmin(FrontendEditableAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Building, BuildingAdmin)
