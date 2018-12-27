from django.contrib import admin
from .models import Set
# Register your models here.
@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display = ['id','setname','setvalue']