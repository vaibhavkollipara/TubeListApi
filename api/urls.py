from django.conf.urls import url
from .views import (
    NewUser,
    UserDetails,
    NewPlaylist,
    PlaylistList,
    PlaylistDetails,
    NewVideo,
    VideoDetail,
    # VideoList,
)
from rest_framework_jwt.views import (
    obtain_jwt_token,
    verify_jwt_token,
    refresh_jwt_token
)

app_name = 'api'

urlpatterns = [

    url(r'^register/$', NewUser.as_view(), name="register"),
    url(r'^authenticate/$', obtain_jwt_token),
    url(r'^authenticate/verify/$', verify_jwt_token),
    url(r'^authenticate/refresh/$', refresh_jwt_token),

    url(r'^user/$', UserDetails.as_view(), name="userdetails"),

    url(r'^newplaylist/$', NewPlaylist.as_view(), name="newplaylist"),
    url(r'^playlists/$', PlaylistList.as_view(), name="playlists"),
    url(r'^playlist/(?P<pk>[0-9]+)/$', PlaylistDetails.as_view(), name="playlistdetails"),
    url(r'^playlist/(?P<pk>[0-9]+)/newvideo/$', NewVideo.as_view(), name="newvideo"),

    # url(r'^playlist/(?P<pk>[0-9]+)/videos/$',VideoList.as_view(),name="videoslist"),
    url(r'^video/(?P<pk>[0-9]+)/$', VideoDetail.as_view(), name='videodetail'),
]
