
from rest_framework.authtoken.views import ObtainAuthToken
from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Profile





class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}, 
        }
    
    def create(self, validated_data):
        
        
        user = User.objects.create(username=validated_data['username'], email=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user



class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    

class SendOtpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ['email', 'phone']


class VerifyOtpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ['email', 'phone', 'otp']
        

    