from rest_framework import serializers
from . import models
class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile object"""

    class Meta:
        model=models.UserProfile
        fields=('id','UserName','email','name','password','phone_no')
        extra_kwargs={'password':{'write_only':True}}


    def create(self,validated_data):
        """Creates and return user"""
        user=models.UserProfile(UserName=validated_data['UserName'],email=validated_data['email'],name=validated_data['name'],phone_no=validated_data['phone_no'])
        user.set_password(validated_data['password'])
        user.save()

        return user


class check_activeSerializer(serializers.Serializer):
    pass
