from django.urls import path
from .views import InboxAPIView


urlpatterns = [
    path('',InboxAPIView.as_view()),
    
]
