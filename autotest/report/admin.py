from django.contrib import admin
from .models import Report
# Register your models here.
@admin.register(Report)
class ApisAdmin(admin.ModelAdmin):
    list_display = [ 'id','name','type', 'path',  'create_time']