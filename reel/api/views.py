from rest_framework import generics
from .serializer import ReelSerializer, ReelDetailSerializer
from ..models import Reel


class ReelAPIView(generics.ListCreateAPIView):
    serializer_class = ReelSerializer
    queryset = Reel.objects.all()


class ReelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReelDetailSerializer
    queryset = Reel.objects.all()


class ReelListFilterByUser(generics.ListAPIView):
    serializer_class = ReelSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Reel.objects.all()
        if user is not None:
            queryset = queryset.filter(
                user__exact=user).order_by('-created_at')
        return queryset
