from django.contrib import admin
from .models import Link
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readOnly_Fields = ('created','updated')
    
admin.site.register(Link, LinkAdmin)
    