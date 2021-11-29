from django.contrib import admin
from .models import *

# Register your models here.


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'experience']
    search_fields = ['name']


class PortfolioLinkAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'project_type']
    search_fields = ['project_name']


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioLink, PortfolioLinkAdmin)
