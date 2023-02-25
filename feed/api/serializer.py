from ..models import Feed, Image, FeedImage, Video, FeedVideo
from rest_framework import serializers


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = "__all__"
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
