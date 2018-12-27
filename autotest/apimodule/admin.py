from django.contrib import admin
from .models import Module
from apitest.models import Apis
# Register your models here.
class ApisAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue','apifunc', 'apimethod', 'apiresult', 'apistatus', 'create_time', 'id',
                    'apimodule']
    model=Apis
    extra = 1
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['modulename','moduledesc','moduler','isexec','create_time','id']
    inlines = [ApisAdmin]