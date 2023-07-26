
from django.urls import path,include
from users.views import *



urlpatterns = [
    
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('send-otp/', SendOtp.as_view(), name='send-otp'),
    path('verify-otp/', VerifyOtp.as_view(), name='verify-otp'),
]