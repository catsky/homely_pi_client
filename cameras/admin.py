from django.contrib import admin

from .models import Image

class ImageAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Created at', {'fields': ['created_at']}),
    ('Location',  {'fields': ['path'], 'classes': ['collapse']})
    ]
  list_display = ('path', 'was_created_recently')
    
admin.site.register(Image, ImageAdmin)