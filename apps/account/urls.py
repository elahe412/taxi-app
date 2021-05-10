from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.account.views import UserCreate
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('signup/', UserCreate.as_view(), name='create_user'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
