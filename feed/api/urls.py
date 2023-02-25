
from django.urls import path
from .views import FeedList, FeedDetail, ImageList, ImageDetail, FeedImageList, VideoList, VideoDetail, FeedVideoList

urlpatterns = [
    path('', FeedList.as_view()),
    path('<int:pk>', FeedDetail.as_view()),
    # path('image/', ImageList.as_view()),
    # path('image/<int:pk>', ImageDetail.as_view()),
    # path('feed-image/', FeedImageList.as_view()),
    # path('video/', VideoList.as_view()),
    # path('video/<int:pk>', VideoDetail.as_view()),
    # path('feed-video/', FeedVideoList.as_view())
]
