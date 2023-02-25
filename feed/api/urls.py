
from django.urls import path
from .views import FeedList,FeedDetail

urlpatterns = [
    path('',FeedList.as_view()),
    path('<int:pk>',FeedDetail.as_view())
]
