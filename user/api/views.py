from rest_framework import generics, permissions
from ..models import User, Follower
from .serializer import *
from django.shortcuts import get_object_or_404


class UserListAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    # permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = User.objects.all()
        user_name = self.request.query_params.get('user_name')
        if user_name is not None:
            queryset = queryset.filter(user_name__exact=user_name)
        return queryset


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FollowerAPIView(generics.ListCreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer


class FollowerCreateAPIVIew(generics.CreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerCreateSerializer


class UnFollowerAPIVIew(generics.ListAPIView):
    queryset = Follower.objects.all()
    serializer_class = UnFollowerSerializer


class FollowerDestroyAPIView(generics.DestroyAPIView):
    serializer_class = FollowerSerializer
    lookup_field = 'followee__user_name'

    def get_queryset(self):
        follower = self.request.user
        followee_username = self.kwargs.get('followee__user_name')
        queryset = Follower.objects.filter(
            follower=follower, followee__user_name=followee_username)
        return queryset

    def perform_destroy(self, instance):
        instance.delete()


class FollowingByUser(generics.ListAPIView):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    def get_queryset(self):
        username = self.request.query_params.get('user_name')
        if username is not None:
            user = User.objects.filter(user_name=username).first()
            queryset = super().get_queryset()
            if user is not None:
                queryset = queryset.filter(
                    follower=user).order_by('-created_at')
            else:
                queryset = queryset.none()  # Return empty queryset if user not found
        return queryset


class FollowerByUser(generics.ListAPIView):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    def get_queryset(self):
        username = self.request.query_params.get('user_name')
        if username is not None:
            user = User.objects.filter(user_name=username).first()
            queryset = super().get_queryset()
            if user is not None:
                queryset = queryset.filter(
                    followee=user).order_by('-created_at')
            else:
                queryset = queryset.none()  # Return empty queryset if user not found
        return queryset
