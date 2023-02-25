

from django.urls import path,include

from .views import UserList,UserDetail

urlpatterns = [
    path('',UserList.as_view()),
    path('<int:pk>',UserDetail.as_view())
]
