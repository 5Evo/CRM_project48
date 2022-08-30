from django.contrib import admin
from .models import Lead, Status, Action, NextAction


# Register your models here.

admin.site.register(Lead)
admin.site.register(Status)
admin.site.register(Action)
admin.site.register(NextAction)