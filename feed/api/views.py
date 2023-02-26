from rest_framework import generics
from ..models import Feed, Image, FeedImage, Video, FeedVideo
from .serializer import FeedSerializer, ImageSerializer, FeedImageSerializer, VideoSerializer, FeedVideoSerializer,FeedCreateSerializer



class FeedCreate(generics.CreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedCreateSerializer

class FeedList(generics.ListAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer


class FeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedCreateSerializer


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class FeedImageList(generics.ListCreateAPIView):
    queryset = FeedImage.objects.all()
    serializer_class = FeedImageSerializer


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class FeedVideoList(generics.ListCreateAPIView):
    queryset = FeedVideo.objects.all()
    serializer_class = FeedVideoSerializer
