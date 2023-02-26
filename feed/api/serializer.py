from ..models import Feed, Image, FeedImage, Video, FeedVideo, FeedLike, FeedSave, Tag
from user.models import User
from rest_framework import serializers, status
from user.api.serializer import UserSerializer
from rest_framework.response import Response


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


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


class FeedSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    has_liked = serializers.SerializerMethodField()
    is_saved = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    carousel_media = serializers.SerializerMethodField()

    def get_has_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False

    def get_is_saved(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.saved.filter(id=request.user.id).exists()
        return False

    def get_tags(self, obj):
        return TagSerializer(obj.tags.all(), many=True).data

    def get_carousel_media(self, obj):
        videos = obj.videos.all()
        images = obj.images.all()
        video_data = VideoSerializer(videos, many=True).data
        images_data = ImageSerializer(images, many=True).data

        return {"videos": video_data, "images": images_data}

    def get_like_count(self, obj):
        return len(UserSerializer(obj.likes.all(), many=True).data)

    class Meta:
        model = Feed
        # fields = '__all__'
        exclude = ('images', 'videos')


class FeedCreateSerializer(serializers.ModelSerializer):
    # likes = serializers.ListField(
    #     child=serializers.IntegerField(), required=False)

    class Meta:
        model = Feed
        exclude = ['user']

    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        print('self.con', self.context['request'].data)
        images = request.FILES.getlist('images')
        videos = request.FILES.getlist('videos')
        print("validated_data", validated_data)
        
        # likes_data = validated_data.pop('likes', [])


        feed = Feed.objects.create(user=user, **validated_data)
        
        # Add likes to the feed
        # for user_id in likes_data:
        #     user = User.objects.get(id=user_id)
        #     feed.likes.add(user)
        # likes = User.objects.filter(id__in=likes_data)
        # feed.likes.set(likes)
        
        
        for image_data in images:
            image = Image.objects.create(src=image_data)
            FeedImage.objects.create(feed=feed, image=image)

        for video_data in videos:
            video = Video.objects.create(src=video_data)
            FeedVideo.objects.create(feed=feed, video=video)

        return feed
