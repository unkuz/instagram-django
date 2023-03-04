from django.urls import path
from .views import MessageAPIView, MessageGroupAPIView


urlpatterns = [
    path('',MessageAPIView.as_view()),
    path('group/',MessageGroupAPIView.as_view())
    
]
