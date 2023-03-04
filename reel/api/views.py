from rest_framework import generics
from .serializer import ReelSerializer, ReelDetailSerializer
from ..models import Reel

class ReelAPIView(generics.ListCreateAPIView):
    serializer_class = ReelSerializer
    queryset = Reel.objects.all()
    
    
class ReelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReelDetailSerializer
    queryset = Reel.objects.all()