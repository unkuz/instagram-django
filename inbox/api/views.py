from rest_framework import generics,serializers
from ..models import Message
from .serializer import MessageSerializer
from django.db.models import Count, Q


class MessageAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    
class MessageGroupSerializer(serializers.Serializer):
    sender_id = serializers.IntegerField()
    sender_name = serializers.CharField()
    recipient_id = serializers.IntegerField()
    recipient_name = serializers.CharField()
    message_count = serializers.IntegerField()


class MessageGroupListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.annotate(
            sender_id=Count('pk', filter=Q(sender=self.context['request'].user)),
            recipient_id=Count('pk', filter=Q(recipient=self.context['request'].user))
        ).values('sender_id', 'sender__username', 'recipient_id', 'recipient__username').order_by()

        serializer = MessageGroupSerializer(data, many=True)
        return serializer.data


class MessageGroupAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    list_serializer_class = MessageGroupListSerializer