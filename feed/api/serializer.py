from ..models import Feed, Image, FeedImage, Video, FeedVideo
from rest_framework import serializers
from user.api.serializer import UserSerializer


class FeedSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    media = serializers.SerializerMethodField()

    def get_media(self, obj):
        return ({"video": VideoSerializer(obj.videos.all(), many=True).data, "image": ImageSerializer(obj.images.all(), many=True).data})

    def get_like_count(self, obj):
        return len(UserSerializer(obj.likes.all(), many=True).data)

    class Meta:
        model = Feed
        exclude = ['videos', 'images']
        depth = 1

    # def create(self, validated_data):
    #     images_data = validated_data.pop('images', [])
    #     feed = Feed.objects.create(**validated_data)
    #     for image_data in images_data:
    #         Image.objects.create(feed=feed, **image_data)
    #     return feed


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class FeedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedImage
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class FeedVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedVideo
        fields = '__all__'
