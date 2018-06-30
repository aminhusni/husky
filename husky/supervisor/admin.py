from django.contrib import admin
from .models import Checklist, Check_item, Supervisor

# Register your models here.
admin.site.register(Checklist)
admin.site.register(Check_item)
admin.site.register(Supervisor)