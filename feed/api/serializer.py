from ..models import Feed, Image, FeedImage, Video, FeedVideo
from rest_framework import serializers
from user.api.serializer import UserSerializer


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
    images = ImageSerializer(many=True, required=False)
    videos = VideoSerializer(many=True, required=False)
    user = UserSerializer(required=False)
    has_liked = serializers.SerializerMethodField()
    is_saved = serializers.SerializerMethodField()

    tags = serializers.SerializerMethodField()

    def get_has_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False

    def get_is_saved(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.save.filter(user=request.user).exists()
        return False

    def get_tags(self, obj):
        return ['Diversity']

    like_count = serializers.SerializerMethodField()
    carousel_media = serializers.SerializerMethodField()

    def get_carousel_media(self, obj):
        return ({"videos": VideoSerializer(obj.videos.all(), many=True).data, "images": ImageSerializer(obj.images.all(), many=True).data})

    def get_like_count(self, obj):
        return len(UserSerializer(obj.likes.all(), many=True).data)

    class Meta:
        model = Feed
        fields = "__all__"

    def create(self, validated_data):
        print("USER", self.context['request'].user)

        request = self.context['request']
        user = request.user
        images = request.FILES.getlist('images')
        videos = request.FILES.getlist('videos')

        print("images", images)

        # images_data = validated_data.pop('images', [])
        # videos_data = validated_data.pop('videos', [])
        feed = Feed.objects.create(user=user, **validated_data)

        for image_data in images:
            image = Image.objects.create(src=image_data)

            a = FeedImage.objects.create(feed=feed, image=image)
            print("A", a)

        for video_data in videos:
            video = Video.objects.create(src=video_data)
            FeedVideo.objects.create(feed=feed, video=video)

        return feed
