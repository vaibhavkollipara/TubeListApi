from django.contrib import admin
from .models import Playlist, Video


class PlaylistModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','created_by','date_created','is_public']
    search_fields = ['name','created_by','date_created']


class VideoModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','playlist', 'date_added']
    search_fields = ['title', 'playlist','date_added']

# Register your models here.
admin.site.register(Playlist,PlaylistModelAdmin)
admin.site.register(Video,VideoModelAdmin)
