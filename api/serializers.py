from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from rest_framework.exceptions import APIException
from myauth.models import SiteUser
from main.models import Playlist, Video
from .util import grabCode, grabVideoDetails


class SiteUserCreateSerializer(ModelSerializer):
    class Meta:
        model = SiteUser
        fields = ['first_name', 'last_name', 'email', 'username', 'password']


class SiteUserDetailSerializer(ModelSerializer):
    class Meta:
        model = SiteUser
        fields = ['first_name', 'last_name', 'email', 'username']


class PlaylistCreateSerializer(ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['name', 'description', 'image_url', 'is_public']


class PlaylistDetailSerializer(ModelSerializer):
    videos = SerializerMethodField()

    class Meta:
        model = Playlist
        fields = ['name', 'description', 'image_url', 'is_public', 'videos']

    def get_videos(self, obj):
        return VideoListSerializer(obj.videolist(), many=True, context={'request': self.context['request']}).data


class PlaylistListSerializer(ModelSerializer):

    video_count = SerializerMethodField()
    createdby = SerializerMethodField()

    class Meta:
        model = Playlist
        fields = ['id', 'name', 'description', 'image_url', 'createdby', 'video_count', 'url']

    url = HyperlinkedIdentityField(
        view_name='api:playlistdetails',
        lookup_field='pk'
    )

    def get_video_count(self, obj):
        return obj.videolist().count()

    def get_createdby(self, obj):
        return obj.created_by.get_full_name()


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ['youtube_url']

    def create(self, validated_data):
        playlist = validated_data['playlist']
        youtube_url = grabCode(validated_data['youtube_url'])
        if youtube_url:
            try:
                (title, thumbnail_url) = grabVideoDetails(youtube_url)
            except:
                raise APIException('Invalid Youtube URL')
            video = Video(playlist=playlist, title=title, thumbnail_url=thumbnail_url, youtube_url=youtube_url)
            try:
                video.save()
            except:
                raise APIException("Seems like video already in playlist !")
        else:
            raise APIException("Invalid Url Provided For Video")
        return validated_data


class VideoListSerializer(ModelSerializer):

    class Meta:
        model = Video
        fields = ['id', 'thumbnail_url', 'title', 'date_added']
