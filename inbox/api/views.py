from rest_framework import generics, serializers
from ..models import Message, Inbox, InboxMessage
from .serializer import InboxSerializer,MessageSerializer
from django.db.models import Count, Q


class InboxAPIView(generics.ListCreateAPIView):
    queryset = Inbox.objects.all()
    serializer_class = InboxSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Inbox.objects.filter(sender=user)
        return queryset

class InboxDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inbox.objects.all()
    serializer_class = InboxSerializer

class MessageAPIView(generics.ListCreateAPIView):
    queryset = InboxMessage.objects.all()
    serializer_class = MessageSerializer