from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class AuthUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            "user_name": user.user_name,
        }
        return Response(data)