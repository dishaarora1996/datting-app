from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.


class Language(models.Model):
    name=models.CharField(max_length=255)
        
    def __str__(self):
        return str(self.name)
        


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    otp = models.CharField(max_length=8, null=True, blank=True)
    date_of_birth = models.DateField(blank=True,null=True)
    language = models.ManyToManyField(Language, related_name="language", blank=True)
    location = models.CharField(max_length=255,blank=True,null=True)
    gender = models.CharField(max_length=100,blank=True,null=True)
    sexual_identity = models.CharField(max_length=100,blank=True,null=True)
    age = models.IntegerField(null=True, blank=True)
    my_lat =  models.CharField(max_length=100,blank=True,null=True)
    my_long =  models.CharField(max_length=100,blank=True,null=True)
    
    min_distance_pref =  models.CharField(max_length=100,blank=True,null=True)
    max_distance_pref =  models.CharField(max_length=100,blank=True,null=True)
    
    gender_pref = models.CharField(max_length=100,blank=True,null=True)
    sexual_identity_pref = models.CharField(max_length=100,blank=True,null=True)
    
    bio = models.DateField(auto_now=False,blank=True,null=True)
    interests = models.CharField(max_length=255,blank=True,null=True)
    dreams = models.CharField(max_length=255,blank=True,null=True)
    relationship_goal = models.CharField(max_length=255,blank=True,null=True)
    hobbies = models.CharField(max_length=255,blank=True,null=True)
    created_on = models.DateField(auto_now_add=True)
    
    
    
    def __str__(self):
        return str(self.email)

    

class ProfileImage(models.Model):
    
    
    def nameFile(instance, filename):
        return '/'.join(['profile', str(instance.profile.id), filename])
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_image")
    image = models.ImageField(upload_to=nameFile, blank=True)
    
    
    def __str__(self):
        return str(self.user.email)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

class BlockedUser(models.Model):
    user_blocked_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_blocked_by")
    blocked_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="blocked_user")
    blocked_on = models.DateTimeField(auto_now_add=True)
    
class UserReports(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="users_report")
    report = models.CharField(max_length=300,blank=True,null=True)
    report_on = models.DateTimeField(auto_now_add=True)

class UserLikes(models.Model):
    who_like = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_like1")
    user_like = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_like2")



# class CustomUserManager(BaseUserManager):
#     """Define a model manager for User model with no username field."""

#     def _create_user(self, email, password=None, **extra_fields):
#         """Create and save a User with the given email and password."""
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password=None, **extra_fields):
#         """Create and save a SuperUser with the given email and password."""
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(email, password, **extra_fields)


# class User(AbstractUser):
#     username = None
#     USERNAME_FIELD = 'email'
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=10,blank=True, null=True)
#     otp = models.IntegerField(blank=True, null=True)
    
#     REQUIRED_FIELDS = []
    
#     objects = CustomUserManager()

#     def __str__(self):
#         return str(self.email)