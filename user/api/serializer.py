from django.contrib.auth import get_user_model
from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_online = serializers.SerializerMethodField()
    has_read_story = serializers.SerializerMethodField()

    def get_has_read_story(self, obj):
        return True

    def get_is_online(self, obj):
        return True

    class Meta:
        model = User
        exclude = ['is_staff']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user
