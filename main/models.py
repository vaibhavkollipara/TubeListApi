from django.db import models
from myauth.models import SiteUser


class Playlist(models.Model):
    created_by = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    image_url = models.CharField(max_length=200)
    is_public = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    def videolist(self):
        return self.video_set.all()

    class Meta:
        ordering = ['-date_created']


class Video(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    thumbnail_url = models.CharField(max_length=200)
    youtube_url = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['youtube_url', 'playlist']
        ordering = ['-date_added', 'playlist']
