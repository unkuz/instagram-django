from django.urls import path
from user.api.views import UserList

urlpatterns = [
    path('user/',UserList.as_view())
]
