from django.contrib import admin
from .models import Reminder
# Register your models here.

class ReminderAdmin(admin.ModelAdmin):
    list_disply = ['title']
    search_fields = ['title']

admin.site.register(Reminder, ReminderAdmin)