from django.urls import path
from .views import StoryListAPIView,StoryCreateAPIView,StoryDetailAPIView

urlpatterns = [
    path('',StoryListAPIView.as_view()),
     path('create/', StoryCreateAPIView.as_view()),
     path('<int:pk>/',StoryDetailAPIView.as_view()),
]
