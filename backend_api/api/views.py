from collections import UserString
from inspect import isroutine
from re import U
from django.shortcuts import render
from django.http import HttpResponse, request
from rest_framework import permissions
from .models import User, Hospital
from rest_framework import viewsets
from .serializers import UserSerializer, HospitalSerializer,UserSerializerWithToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.hashers import make_password
from api import serializers
from rest_framework import status



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
   def validate(self, attrs):
       data =  super().validate(attrs)
       
       serializer = UserSerializerWithToken(self.user).data
       for k, v in serializer.items():
           data [k] = v
       return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerUser(request):
    data = request.data
    
    try:
        user = User.objects.create(
            first_name = data['name'],
            username = data['email'],
            email= data['email'],
            password = make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail' : 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    users = request.user
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUSers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


def index(requst):
    return HttpResponse("yes its working properly")
