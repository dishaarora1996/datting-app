
from api.models import *
from api.serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser #file imag upload



# Create your views here.
        
# class UserProfile(APIView):
    
#     def get(self, request, pk):
#         try:
#             profile = Profile.objects.get(id=pk)
#         except:
#             return Response({'error':'No profile found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
        
#         try:
#             profile = Profile.objects.get(id=pk)
#         except:
#             return Response({'error':'No profile found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ProfileSerializer(profile, data=request.data)
#         if serializer.is_valid():
#             profile = serializer.save()
            
#             languages =request.data.pop('language', [])
#             print(languages)

#             if len(languages):
#                 for language in languages:
#                     lang=Language.objects.filter(name=language)
#                     profile.language.add(lang)

#                 profile.save()
            
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def update_profile(request, pk=None):
    try:
        profile = Profile.objects.get(id=pk)
    except Profile.DoesNotExist:
        raise NotFound()
    serializer = ProfileSerializer(profile, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    print("Hi")
    
    tags = []
    language = request.data.get('language')
    if len(language):
        for tag in language:
            tag = Language.objects.get(name=tag)
            tags.append(tag)
    profile.language.set(tags)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

            
class UserProfile(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
        

class UploadImage(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def get(self, request):
        profiles = ProfileImage.objects.all()
        serializers = ProfileImageSerializer(profiles, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ProfileImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)
  

    
    
    
    
    
    
    
    
    
    
    
    
    


class Verifyotp(APIView):
    def post(self, request, formate=None):
        serializer = VerifyOtpSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.data.get('phone')
            otp = serializer.data.get('otp')
            if User.objects.filter(phone=phone,otp=otp).exists():
                return Response({'msg':'Account Verify'},serializer.data,status=status.HTTP_200_OK)
            return Response({'msg':'OTP Verification Faild.'},status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class Showuser(APIView):
    def get(self, request, pk):
        try:
            id = pk 
            cl1 = User.objects.filter(pk=id)
        except:
            return Response({'error':'wrong id'}, status=status.HTTP_200_OK)
        serializer = ShowSerializer(cl1, many=True)
        # userid = serializer.data.get('id')
        # usersimg = images.objects.filter(id=userid)
        # serializer2 = imagesSerializer(usersimg, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class Blockuser(APIView):
    def post(self, request, formate=None):
        serializer = BlockUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'User Blocked success'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

class Reportuser(APIView):
    def post(self, request, formate=None):
        serializer = UserReportsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'User Report Add success'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

class UserLikes(APIView):
    def post(self, request, formate=None):
        serializer = UserLikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'User Liked success'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    
    




# class userprofile(APIView):
#     def get(self, request, pk,formate=None):
#         try:
#             id = pk 
#             cl1 = User.objects.filter(pk=id)
#         except:
#             return Response({'error':'wrong id'}, status=status.HTTP_200_OK)
#         serializer = ProfileSerializer(cl1, many=True)
#         #uid = serializer.data.get('id')
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def put(self, request, pk, format=None):
#         try:
#             id = pk 
#             cl1 = ProfileSerializer.objects.get(pk=id)
#         except:
#             return Response({'error':'wrong id'}, status=status.HTTP_200_OK)
#         serializer = ProfileSerializer(cl1, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Update'}, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.error, status=status.HTTP_200_OK)



# class loginuser(APIView):
#     #renderer_classes = [UserRenderer]
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         print('email:', request.data)
#         if serializer.is_valid():
#             email = serializer.data.get('email')
#             password = serializer.data.get('password')
#             print('email:', email)
#             user = authenticate(email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 users = request.user.id
#                 #user_type = request.user.user_type
#                 return Response({'msg':'Login Success','user_id':users}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'msg':'Email or Password is not Valid'}, status=status.HTTP_200_OK)
#         return Response(serializer.error, status=status.HTTP_404_NOT_FOUND) 

