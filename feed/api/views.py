from rest_framework import generics
from ..models import Feed
from .serializer import FeedSerializer

class FeedList(generics.ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    
class FeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer