from django.urls import path
from .views import StoryListAPIView,StoryCreateAPIView

urlpatterns = [
    path('',StoryListAPIView.as_view()),
     path('create/', StoryCreateAPIView.as_view()),
]
