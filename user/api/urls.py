

from django.urls import path

from .views import *


urlpatterns = [
    path('', UserListAPIView.as_view()),
    path('<int:pk>/', UserDetailAPIView.as_view()),
    path('follower/', FollowerAPIView.as_view()),
    path('follower/create/', FollowerCreateAPIVIew.as_view()),
    path('follower/unfollow/<str:followee__user_name>/',
         FollowerDestroyAPIView.as_view()),
    path('following-by-user/', FollowingByUser.as_view()),
    path('follower-by-user/', FollowerByUser.as_view()),
]
