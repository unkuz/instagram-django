
from django.urls import path
from .views import *

urlpatterns = [
    path('', FeedList.as_view()),
    path('create/', FeedCreate.as_view()),
    path('<int:pk>/', FeedDetail.as_view()),
    path('comment/', FeedComment.as_view()),
    path('like/', FeedLikeAPIView.as_view()),
    path('save/', FeedSaveAPIView.as_view()),
]
