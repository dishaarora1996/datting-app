from .models import *
from django.core.exceptions import ValidationError
import requests, json
from rest_framework import serializers
from .models import Profile



class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'

class ProfileImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProfileImage
        fields = '__all__'
        

class ProfileSerializer(serializers.ModelSerializer):
    profile_image = ProfileImageSerializer(many=True, read_only=True)
    # language = serializers.ListField(child = serializers.CharField())
    language = LanguageSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
        exclude_fields=('user',)
        
    # def update(self, instance, validated_data):
    #     print(instance.language.all())
    #     instance.language.clear()
    #     languages = validated_data.pop('language', [])
    #     print(languages)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     if len(languages):
    #         for language in languages:
    #             print(language)
    #             al=Language.objects.get(name=language)
    #             print(al)
    #             instance.language.add(al)
    #             print("ok")
    #     return instance
    
    
    
    
    # # def create(self, validated_data):

    # #     languages =validated_data.pop('language', [])

    # #     profile=Profile.objects.create(**validated_data)
    # #     if len(languages):
    # #         for language in languages:

    # #             lang=Language.objects.filter(name=language)
    # #             profile.allergies.add(lang)

    # #         profile.save()
    # #         return profile

    # def save(self, **kwargs):
    #     language = self.validated_data.pop('language', [])
    #     # profile = Profile.objects.create(**self.validated_data)

    #     if len(language):
    #         language_objs = []
    #         for language_name in language:
    #             language_obj, created = Language.objects.get_or_create(name=language_name)
    #             language_objs.append(language_obj)
    #             profile.language.add(language_obj)
    #             profile.save()
    

















class ShowSerializer(serializers.ModelSerializer):
    #user = imagesSerializer()
    class Meta:
        model = User
        fields = '__all__'



# def PushSMS(phone,otp):
#     try:
#         url = "https://2factor.in/API/V1/cded9a58-d835-11ed-addf-0200cd936042/SMS/9981373591/{otp}/OTP"

#         payload=''
#         headers = {}

#         response = requests.request("POST", url, headers=headers, data=payload)

#         print(response.text)

#         # param= {
#         # "user":user,
#         # "password":password,
#         # "msisdn":msisdn,
#         # "sid":sid,
#         # "msg":msg,
#         # "fl":fl,
#         # "gwid":gwid,
#         # }
#         # url="https://getwaysms.com/vendorsms/pushsms.aspx"
#         # response = requests.get(url,param)
#     except requests.exceptions.RequestException as e:
#         print("Exception Occur:%s"%e)
#         raise (e)

        

    
class VerifyOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone','otp']



class BlockUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockedUser
        fields = '__all__'

class UserReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReports
        fields = '__all__'

class UserLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLikes
        fields = '__all__'
        
        




# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#         #fields = ['email','password','phone','location']

    # def create(self, validated_data):
    #     user = super(RegisterSerializer, self).create(validated_data)
    #     user.set_password(validated_data['password'])
    #     otp = random.randint(1111, 9999)
    #     user.otp = otp
    #     # url = "https://2factor.in/API/R1/"
    #     # msg = f"Your OTP for verification is ({otp}). This OTP is valid for XXXX minutes. Please do not share this OTP with anyone."
    #     url = f"https://2factor.in/API/V1/cded9a58-d835-11ed-addf-0200cd936042/SMS/{user.phone}/{otp}/OTP"
    #     payload=  '' #'module=&apikey=cded9a58-d835-11ed-addf-0200cd936042&to=919981373591&from=VRVAPP&msg={msg}'
    #     headers = {}
    #     response = requests.request("POST", url, headers=headers, data=payload)
    #     print(response.text)
    #     user.save()
    #     return user