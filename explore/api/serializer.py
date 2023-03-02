from rest_framework import serializers
from feed.models import Feed
from story.models import Story,Image

from story.api.serializer import ImageSerializer

class ExploreSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = Feed
        fields = '__all__'
    