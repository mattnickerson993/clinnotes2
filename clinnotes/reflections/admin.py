from django.contrib import admin
from .models import Reflection, GuidedReflection
# Register your models here.

class ReflectionAdmin(admin.ModelAdmin):
    list_disply = ['title']
    search_fields = ['title']

admin.site.register(Reflection, ReflectionAdmin)
admin.site.register(GuidedReflection)