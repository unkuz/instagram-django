from django.urls import path
from user.api.views import UserListAPIView

urlpatterns = [
    path('user/',UserListAPIView.as_view())
]
