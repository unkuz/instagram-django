from django.urls import path
from .views import InboxAPIView, MessageAPIView, InboxDetailAPIView


urlpatterns = [
    path('', InboxAPIView.as_view()),
    path('send/', MessageAPIView.as_view()),
    path('<int:pk>/', InboxDetailAPIView.as_view())

]
