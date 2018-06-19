from django.contrib import admin

# Register your models here.
from app_poc.models import Hit


@admin.register(Hit)
class HitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
