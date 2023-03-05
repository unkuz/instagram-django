from rest_framework import generics, serializers
from ..models import Message, Inbox
from .serializer import InboxSerializer
from django.db.models import Count, Q


class InboxAPIView(generics.ListCreateAPIView):
    queryset = Inbox.objects.all()
    serializer_class = InboxSerializer
