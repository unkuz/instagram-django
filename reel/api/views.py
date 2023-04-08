from rest_framework import generics
from .serializer import ReelSerializer, ReelDetailSerializer
from ..models import Reel
from user.models import User


class ReelAPIView(generics.ListCreateAPIView):
    serializer_class = ReelSerializer
    queryset = Reel.objects.all()


class ReelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReelDetailSerializer
    queryset = Reel.objects.all()


class ReelListFilterByUser(generics.ListAPIView):
    serializer_class = ReelSerializer
    queryset = Reel.objects.all()

    def get_queryset(self):
        username = self.request.query_params.get('user_name')
        if username is not None:

            user = User.objects.filter(user_name=username).first()
            queryset = super().get_queryset()
            if user is not None:
                queryset = queryset.filter(user=user).order_by('-created_at')
            else:
                queryset = queryset.none()  # Return empty queryset if user not found
        return queryset
