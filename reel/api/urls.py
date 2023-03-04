from django.urls import path

from .views import ReelAPIView, ReelDetailAPIView

urlpatterns = [
    path('',ReelAPIView.as_view()),
    path('<int:pk>/',ReelDetailAPIView.as_view())
]
