from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        credentials = {
            'user_name': attrs.get(User.USERNAME_FIELD),
            'password': attrs.get('password')
        }

        user = authenticate(**credentials)

        if user is None:
            raise serializers.ValidationError('Invalid username or password')

        if not user.is_active:
            raise serializers.ValidationError('User account is disabled')

        token = super().validate(attrs)
        token['user'] = user

        return token