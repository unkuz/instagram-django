from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.api.serializer import UserSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        key_data = ['access', 'refresh']
        access = data[key_data[0]]
        refresh = data[key_data[1]]

        data['token'] = {
            'access': access,
            "refresh": refresh
        }

        for key in key_data:
            data.pop(key, None)

        user_name = self.user.user_name
        profile_pic_url = str(self.user.profile_pic_url)
        cover_pic_url = str(self.user.cover_pic_url)

        data['user'] = {
            "user_name": user_name,
            "profile_pic_url": profile_pic_url,
            "cover_pic_url": cover_pic_url

        }

        return data
