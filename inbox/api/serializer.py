from rest_framework import serializers
from ..models import Message, Inbox, InboxMessage
from operator import attrgetter
from user.models import User
from user.api.serializer import UserSerializer


class InboxSerializer(serializers.ModelSerializer):
    # sender = UserSerializer()
    # recipient = UserSerializer()

    class Meta:
        model = Inbox
        fields = '__all__'
        read_only_fields = ['sender', 'recipient']
        depth = 2

    def create(self, validated_data):
        request = self.context['request']
        user, data = attrgetter('user', 'data')(request)
        recipient = data['recipient']

        if not user.is_authenticated:
            raise serializers.ValidationError('Not valid user send')

        recipient_user = User.objects.filter(user_name__exact=recipient)

        if not recipient_user.exists():
            raise serializers.ValidationError('Recipient not valid')

        if recipient_user.first() is user:
            raise serializers.ValidationError(
                'Only accept send to other person')
            
        check = Inbox.objects.filter(sender = user,recipient =  recipient_user.first()).exists()
        
        if check:
            return {}

        inbox = Inbox.objects.create(
            sender=user, recipient=recipient_user.first(), **validated_data)

        return inbox


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InboxMessage
        fields = '__all__'
        read_only_fields =['inbox','message']

    def create(self, validated_data):
        request = self.context['request']
        user, data = attrgetter('user', 'data')(request)
        inbox_id = data.get('inbox')
        message_content = data.get('message')

        if not user.is_authenticated:
            raise serializers.ValidationError('Not valid user send')

        inbox = Inbox.objects.filter(id=inbox_id).first()

        if inbox:
            message = Message.objects.create(
                content=message_content, user=user)
            instance = InboxMessage.objects.create(
                inbox=inbox, message=message)
            return instance
        else:
            raise serializers.ValidationError('Inbox not found')
