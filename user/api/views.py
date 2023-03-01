from rest_framework import generics, permissions
from ..models import User 
from .serializer import UserSerializer

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        queryset = User.objects.all()
        user_name = self.request.query_params.get('user_name')
        if user_name is not None:
            queryset = queryset.filter(user_name__exact = user_name)
        return queryset
    
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer