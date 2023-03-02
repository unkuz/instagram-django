from rest_framework import generics
from ..models import Story
from ..api.serializer import StorySerializer, StoryCreateSerializer


class StoryListAPIView(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    
class StoryCreateAPIView(generics.CreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryCreateSerializer