from django.urls import path,include

from .views import ExploreListAPIView


urlpatterns = [
    path('',ExploreListAPIView.as_view())
]
