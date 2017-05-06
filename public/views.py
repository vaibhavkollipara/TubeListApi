from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter
from .serializers import PlaylistListSerializer, PlaylistDetailSerializer, VideoSerializer
from main.models import Playlist, Video
from api.paginations import MyPageNumberPagination


class Playlists(ListAPIView):
    """
    Api endpoint to retrieve all public playlists
    """
    serializer_class = PlaylistListSerializer
    queryset = Playlist.objects.filter(is_public=True)
    permission_classes = [AllowAny]
    pagination_class = MyPageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['name']


class PlaylistDetails(RetrieveAPIView):
    """
    Api to view retrieve playlist details
    """
    serializer_class = PlaylistDetailSerializer
    permission_classes = [AllowAny]
    queryset = Playlist.objects.filter(is_public=True)


class VideoDetail(RetrieveAPIView):
    """
    Api endpoint to view video details
    """
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs_playlist = Playlist.objects.filter(is_public=True)
        qs_videos = Video.objects.none()
        for playlist in qs_playlist:
            qs_videos = qs_videos | playlist.videolist()
        return qs_videos
