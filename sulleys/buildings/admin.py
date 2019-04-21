from django.contrib import admin

from cms.admin.placeholderadmin import FrontendEditableAdminMixin

from buildings import models


class BuildingImageAdmin(admin.TabularInline):
    model = models.BuildingImage


class BuildingAdmin(FrontendEditableAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [BuildingImageAdmin]


admin.site.register(models.Building, BuildingAdmin)
