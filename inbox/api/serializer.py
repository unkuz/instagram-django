from rest_framework import serializers
from ..models import Message
from operator import attrgetter
from user.models import User
from user.api.serializer import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    # sender = UserSerializer()
    # recipient = UserSerializer()
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['sender','recipient']
    
        
    def create(self,validated_data):
        request = self.context['request']
        user, data = attrgetter('user','data')(request)
        recipient = data['recipient']
        
        if not user.is_authenticated:
            raise serializers.ValidationError('Not valid user send')
        
        recipient_user =  User.objects.filter(user_name__exact = recipient)
        
        if not recipient_user.exists():
            raise serializers.ValidationError('Recipient not valid')
        
        if recipient_user.first() is user:
            raise serializers.ValidationError('Only accept send to other person')
        
        message = Message.objects.create(sender = user, recipient= recipient_user.first(), **validated_data)
        
        return message
        
        
        
        
        
    
        