from django.contrib.auth import get_user_model
from rest_framework import serializers, status
from ..models import User, Follower
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_online = serializers.SerializerMethodField()
    has_read_story = serializers.SerializerMethodField()

    is_follow = serializers.SerializerMethodField()

    def get_has_read_story(self, obj):
        return True

    def get_is_online(self, obj):
        return True

    def get_is_follow(self, obj):
        request = self.context.get('request')
        if request is not None and hasattr(request, 'user'):
            checkExist = Follower.objects.filter(
                follower=request.user, followee=obj).first()
            if checkExist is None:
                return False
            return True
        else:
            return False

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

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = '__all__'
        depth = 1


class FollowerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        exclude = ['follower']

    def create(self, validated_data):
        request = self.context.get('request')
        follower = request.user

        checkExist = Follower.objects.filter(**validated_data,
                                             follower=follower).first()

        if checkExist is None:
            instance = Follower.objects.create(
                **validated_data, follower=follower)
            return instance
        raise serializers.ValidationError("Exist one")


class UnFollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        exclude = ['follower']

    def delete(self, validated_data):
        print("HEEH")
        request = self.context.get('request')
        follower = request.user

        checkExist = Follower.objects.filter(
            **validated_data, follower=follower).first()

        print("check", checkExist)

        if checkExist:
            checkExist.delete()
        else:
            raise serializers.ValidationError('No exists')
