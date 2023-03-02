from rest_framework import generics
from feed.models import Feed
from story.models import Story
from .serializer import ExploreSerializer
from itertools import chain

from .serializer import ExploreSerializer

class ExploreListAPIView(generics.ListAPIView):
    serializer_class = ExploreSerializer
    
    def get_queryset(self):
        return Feed.objects.all()
    