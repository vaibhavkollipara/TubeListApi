from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveDestroyAPIView
)
from rest_framework.filters import SearchFilter
from .permissions import IsPlaylistOwner, IsCurrentUser
from .serializers import (
    SiteUserCreateSerializer,
    SiteUserDetailSerializer,
    PlaylistCreateSerializer,
    PlaylistDetailSerializer,
    PlaylistListSerializer,
    VideoSerializer,
    # VideoListSerializer
)
from .paginations import MyPageNumberPagination
from myauth.models import SiteUser
from main.models import Playlist, Video


class NewUser(CreateAPIView):
    """
    Api endpoint to create new playlist
    """
    serializer_class = SiteUserCreateSerializer
    permission_classes = [AllowAny]


class UserDetails(RetrieveAPIView):
    """
    Api endpoint to get logged in user details
    """
    serializer_class = SiteUserDetailSerializer

    def get(self, request, *args, **kwargs):
        siteUser = SiteUser.objects.get(username=request.user.username)
        serializer = self.get_serializer(siteUser)
        return Response(serializer.data)


class NewPlaylist(CreateAPIView):
    """
    Api endpoint to create new playlist
    """
    serializer_class = PlaylistCreateSerializer

    def perform_create(self, serializer):
        user = SiteUser.objects.get(username=self.request.user.username)
        serializer.save(created_by=user)


class PlaylistList(ListAPIView):
    """
    Api endpoint to retrieve user specific playlists
    """
    serializer_class = PlaylistListSerializer
    pagination_class = MyPageNumberPagination

    def get_queryset(self):
        user = SiteUser.objects.get(username=self.request.user.username)
        qs = Playlist.objects.filter(created_by=user)
        return qs


class PlaylistDetails(RetrieveUpdateDestroyAPIView):
    """
    Api to view, update and delete playlist
    """
    serializer_class = PlaylistDetailSerializer

    def get_queryset(self):
        user = SiteUser.objects.get(username=self.request.user.username)
        qs = Playlist.objects.filter(created_by=user)
        return qs


class NewVideo(CreateAPIView):
    """
    Api endpoint to add new video to playlist
    """
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'

    def perform_create(self, serializer):
        playlist_id = self.kwargs.get(self.lookup_url_kwarg)
        try:
            playlist = Playlist.objects.get(pk=playlist_id)
        except:
            raise APIException("Invalid Playlist")
        user = SiteUser.objects.get(username=self.request.user.username)
        if playlist.created_by != user:
            raise APIException('Not your playlist')
        serializer.save(playlist=playlist)


class VideoDetail(RetrieveDestroyAPIView):
    """
    Api endpoint to view, update and delete video details
    """
    serializer_class = VideoSerializer

    def get_queryset(self):
        user = SiteUser.objects.get(username=self.request.user.username)
        qs_playlist = user.playlist_set.all()
        qs_videos = Video.objects.none()
        for playlist in qs_playlist:
            qs_videos = qs_videos | playlist.videolist()
        return qs_videos

        # class VideoList(ListAPIView):
        #     serializer_class = VideoListSerializer
        #
        #     def get_queryset(self):
        #         playlist_id = self.kwargs.get(self.lookup_url_kwarg)
        #         try:
        #             playlist = Playlist.objects.get(pk=playlist_id)
        #         except:
        #             raise APIException("Invalid Playlist")
        #         return playlist.videolist()
