from django.urls import path

from .views import *

urlpatterns = [
    path('', ReelAPIView.as_view()),
    path('<int:pk>/', ReelDetailAPIView.as_view()),
    path('by-user/', ReelListFilterByUser.as_view())
]
