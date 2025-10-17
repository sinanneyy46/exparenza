from django.contrib import admin
from .models import Result, GalleryImage, Headline

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'zone', 'published', 'created_at')
    list_filter = ('published',)
    search_fields = ('event_name', 'zone')

@admin.register(GalleryImage)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'uploaded_at')
    list_filter = ('published',)

@admin.register(Headline)
class HeadlineAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'content', 'published', 'created_at')
    list_filter = ('published',)
