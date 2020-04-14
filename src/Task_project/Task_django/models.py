from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self,UserName,name,email,phone_no,password=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError('Users must have email address')

        email=self.normalize_email(email)
        """Converts all character to lower case"""
        user=self.model(UserName=UserName,email=email,name=name,phone_no=phone_no)

        user.set_password(password)
        """encrypts the password"""
        user.save(using=self._db)

        return user

    def create_superuser(self,UserName,name,email,phone_no,password):
        """Creates and saves a new superuser with given details."""

        user=self.create_user(UserName,name,email,phone_no,password)
        user.is_superuser=True
        user.is_staff=True

        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a "user profile" inside our system"""
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255,unique=True)
    phone_no=models.CharField(max_length=10,unique=True)
    UserName=models.CharField(max_length=255,unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='UserName'
    REQUIRED_FIELDS=['name','email','phone_no']

    def get_full_name(self):
        """Used to get users a full name."""

        return self.name

    def __str__(self):
        """Django uses this when it needs to convert object to a string"""

        return self.UserName
