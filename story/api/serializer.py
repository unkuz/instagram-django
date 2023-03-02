
from rest_framework import serializers
from user.api.serializer import UserSerializer
from ..models import Video, Image, Story, StoryImage, StoryVideo

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class StorySerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    has_liked = serializers.SerializerMethodField()
    is_saved = serializers.SerializerMethodField()
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
    
    def get_carousel_media(self, obj):
        videos = obj.videos.all()
        images = obj.images.all()
        video_data = VideoSerializer(videos, many=True).data
        images_data = ImageSerializer(images, many=True).data

        return {"videos": video_data, "images": images_data}

    def get_like_count(self, obj):
        return len(UserSerializer(obj.likes.all(), many=True).data)

    class Meta:
        model = Story
        exclude = ('images', 'videos')

class StoryCreateSerializer(serializers.ModelSerializer):
    # likes = serializers.ListField(
    #     child=serializers.IntegerField(), required=False)

    class Meta:
        model = Story
        exclude = ['user']
        
    def update(self, instance, validated_data):
        print("KAKA",validated_data["images"])
        # instance.caption_text = validated_data.get()
        
        print("HEHEHE")
        print("instance",instance)
        return instance

    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        print('self.con', self.context['request'].data)
        images = request.FILES.getlist('images')
        videos = request.FILES.getlist('videos')
        print("validated_data", validated_data)
        
        # likes_data = validated_data.pop('likes', [])


        feed = Story.objects.create(user=user, **validated_data)
        
        # Add likes to the feed
        # for user_id in likes_data:
        #     user = User.objects.get(id=user_id)
        #     feed.likes.add(user)
        # likes = User.objects.filter(id__in=likes_data)
        # feed.likes.set(likes)
        
        
        for image_data in images:
            image = Image.objects.create(src=image_data)
            StoryImage.objects.create(feed=feed, image=image)

        for video_data in videos:
            video = Video.objects.create(src=video_data)
            StoryVideo.objects.create(feed=feed, video=video)

        return feed