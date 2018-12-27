from django.contrib import admin
from .models import Apitest,Apis
# Register your models here.



@admin.register(Apitest)
class ApitestAdmin(admin.ModelAdmin):
    list_display = ['apitestname','apitestdesc','apitestparamsvalue','apitestfunc', 'apitester', 'apitestresult', 'apitestexec','create_time', 'id']

@admin.register(Apis)
class ApisAdmin(admin.ModelAdmin):
    list_display = ['apiname', 'apiurl', 'apiparamvalue','apifunc', 'apimethod', 'apiresult', 'apiexec', 'create_time', 'id',
                    'apimodule']