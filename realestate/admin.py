from django.contrib import admin
from .models import Estate

class EstateAdmin(admin.ModelAdmin):
    list_display = ['type', 'state', 'city', 'region', 'street', 'main_alley', 'side_alley', 'building_number', 'building_name', 'postal_code', 'floor', 'unit', 'elevator', 'parking', 'warehouse', 'swimming_pool', 'year_created', 'area', 'price', 'description']
    list_display_links = ['type', 'state', 'city', 'region', 'street', 'main_alley', 'side_alley', 'building_number', 'building_name', 'postal_code', 'floor', 'unit', 'elevator', 'parking', 'warehouse', 'swimming_pool', 'year_created', 'area', 'price', 'description']
    list_per_page = 10
    prepopulated_fields = {"slug": ("city", "street", "building_name")}

admin.site.register(Estate, EstateAdmin)

  