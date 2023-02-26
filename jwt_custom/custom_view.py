from rest_framework_simplejwt.views import TokenObtainPairView
from .custom_serializer import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    