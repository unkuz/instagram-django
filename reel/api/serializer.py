from rest_framework import serializers
from ..models import Reel, Video, ReelVideo
from operator import attrgetter
import pydash as _
from utils.validate.file import is_video
from user.api.serializer import UserSerializer


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class ReelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reel
        fields = '__all__'
        read_only_fields = ['user', 'videos', 'likes',
                            'saved', 'comments', 'tags', 'seen']

    videos = VideoSerializer(many=True)
    user = UserSerializer()

    def create(self, validated_data):
        request = self.context['request']
        user, data, FILES = attrgetter('user', 'data', 'FILES')(request)
        videos = FILES.getlist('videos')

        if not user.is_authenticated:
            raise serializers.ValidationError('user is not valid')

        if _.is_empty(videos):
            raise serializers.ValidationError('videos field is required')
        else:
            print("NOT NONE")

        reel = Reel.objects.create(user=user, **validated_data)

        for i in videos:
            if not is_video(i):
                raise serializers.ValidationError(
                    'Not valid video or video is heavy')

        for i in videos:
            video = Video.objects.create(src=i)
            ReelVideo.objects.create(reel=reel, video=video)

        return reel


class ReelDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    videos = VideoSerializer(many=True)

    class Meta:
        model = Reel
        fields = '__all__'
