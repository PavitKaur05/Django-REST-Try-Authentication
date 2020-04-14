from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from . import serializers
from . import models
# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """Registering a new user"""

    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes= (TokenAuthentication,)

class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token and other bio details"""
    serializer_class=AuthTokenSerializer
    def create(self,request):
        """Use the ObtainAuthToken APIView to validate and create a token."""
        return CustomAuthToken().post(request)



class CustomAuthToken(ObtainAuthToken):
    """A Custom Auth Token Class so other bio details can be displayed"""
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'name':user.name,
            'email': user.email,
            'phoneNo':user.phone_no
        })

class check_active(viewsets.ModelViewSet):
    """Endpoint to check that server is active """
    serializer_class=serializers.check_activeSerializer
    def list(self,request):
        return Response({'status':'OK'})
