from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

urlpatterns = [
    # Email verification endpoint
    path('auth/registration/account-confirm-email/<key>/', AutoVerifyEmailView.as_view(), name='account_confirm_email'),
    
    # Google OAuth2 login endpoint
    path('auth/google/login/', GoogleLoginView.as_view(), name='google_login'),
    
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]