from django.urls import path,include
from api.views import *


urlpatterns = [
    
    path('upload-image/', UploadImage.as_view(), name='upload-image'),
    path('user-profile/<int:pk>', update_profile, name='user-profile'),
    
    
    
    
    
    
    
    
    path('otp-verify/', Verifyotp.as_view(), name='Verifyotp'),
    path('show-user/<int:pk>/', Showuser.as_view(), name='Showuser'),
    path('block-user/', Blockuser.as_view(), name='Blockuser'),
    path('report-user/<int:pk>/', Reportuser.as_view(), name='Reportuser'),
    path('user-likes/', UserLikes.as_view(), name='UserLikes'),
    
    
    # path('<int:pk>/', userprofile.as_view(), name='userprofile'),
    # path('login/', loginuser.as_view(), name='loginuser'),
    # path('update/<int:pk>/', register.as_view(), name='register'),
]