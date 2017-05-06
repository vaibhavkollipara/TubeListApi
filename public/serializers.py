from rest_framework.serializers import ModelSerializer, SerializerMethodField, HyperlinkedIdentityField
from main.models import Playlist, Video


class PlaylistListSerializer(ModelSerializer):

    video_count = SerializerMethodField()
    createdby = SerializerMethodField()

    class Meta:
        model = Playlist
        fields = ['id', 'name', 'image_url', 'createdby', 'video_count']

    def get_video_count(self, obj):
        return obj.videolist().count()

    def get_createdby(self, obj):
        return obj.created_by.get_full_name()


class PlaylistDetailSerializer(ModelSerializer):
    videos = SerializerMethodField()
    createdby = SerializerMethodField()

    class Meta:
        model = Playlist
        fields = ['name', 'description', 'createdby', 'image_url', 'videos']

    def get_createdby(self, obj):
        return obj.created_by.get_full_name()

    def get_videos(self, obj):
        return VideoListSerializer(obj.videolist(), many=True, context={'request': self.context['request']}).data


class VideoListSerializer(ModelSerializer):

    class Meta:
        model = Video
        fields = ['id', 'thumbnail_url', 'title', 'date_added']


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ['title', 'youtube_url']
