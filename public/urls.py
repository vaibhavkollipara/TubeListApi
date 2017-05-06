from django.conf.urls import url
from .views import Playlists, PlaylistDetails, VideoDetail

app_name = "public"

urlpatterns = [
    url(r'^playlists/$', Playlists.as_view(), name="publicplaylists"),
    url(r'^playlist/(?P<pk>[0-9]+)/$', PlaylistDetails.as_view(), name="playlistdetail"),
    url(r'^video/(?P<pk>[0-9]+)/$', VideoDetail.as_view(), name="videodetail"),
]
