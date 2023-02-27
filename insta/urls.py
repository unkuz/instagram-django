from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from jwt_custom.custom_view import CustomTokenObtainPairView
from jwt_custom.user_view import AuthUserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', AuthUserView.as_view(), name='get_current_user'),
    path('user/',include('user.api.urls')),
    path('feed/',include('feed.api.urls'))
    
    
]
