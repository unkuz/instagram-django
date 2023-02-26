
from django.urls import path
from .views import FeedList, FeedDetail,FeedCreate, ImageList, ImageDetail, FeedImageList, VideoList, VideoDetail, FeedVideoList

urlpatterns = [
    path('', FeedList.as_view()),
    path('create/', FeedCreate.as_view()),
    path('<int:pk>', FeedDetail.as_view()),
]
