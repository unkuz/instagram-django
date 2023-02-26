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
        img_avatar = str(self.user.img_avatar)
        img_cover = str(self.user.img_cover)

        data['user'] = {
            "user_name": user_name,
            "img_avatar": img_avatar,
            "img_cover": img_cover

        }

        return data
