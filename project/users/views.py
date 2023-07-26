from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .utils import send_otp_to_phone

# Create your views here.


class RegisterUser(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user_account = serializer.save()
            data['response'] = 'Registration Successful!'
            data['username'] = user_account.email
            # token = Token.objects.get(user=user_account).key
            # data['token'] = token
            return Response(data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# for login using token_authentication
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data,
                                       context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # token, created = Token.objects.get_or_create(user=user)
        return Response({
            # 'token': token.key,
            # 'user_id': user.pk,
            'username': user.email
        })


class LogoutUser(APIView):

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)




class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"error": "Incorrect password"}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendOtp(APIView):

     def put(self, request):

        try:
            profile = Profile.objects.get(email=request.data['email'])
        except:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SendOtpSerializer(profile, data=request.data)
        if serializer.is_valid():
            otp = send_otp_to_phone(request.data['phone'])
            profile = serializer.save()
            profile.otp = otp
            profile.save()
            return Response({"response": "Otp sent successful!"},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VerifyOtp(APIView):

     def patch(self, request):
        try:
            profile = Profile.objects.get(email=request.data['email'], phone=request.data['phone'])
        except:
            return Response({"error": "Incorrect email or phone"}, status=status.HTTP_404_NOT_FOUND)
        serializer = VerifyOtpSerializer(profile, data=request.data)
        data = {}
        if serializer.is_valid():
            if profile.otp == request.data['otp']:
                profile.otp = 'verified'
                profile.save()
                token = Token.objects.get(user=profile.user).key
                data['token'] = token
                return Response(data,status=status.HTTP_200_OK)
            return Response({"response": "Incorrect Otp"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



