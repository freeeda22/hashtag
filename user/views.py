from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate, logout, login
import re
class SignupAPIView(APIView):
    """
        View for user creation
    """
    permission_classes = [] #disables permission
    serializer_class = UserCreateSerializer

    def post(self,request):
        data=request.data
        print("data.....1.....",data)
        mobile = data['mobile']
        # mobileValid(mobile)
        Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
        valid_mobile=Pattern.match(mobile)
        if(valid_mobile==None):
            return Response("Enter a valid mobile number")
        else:
            serializer= UserCreateSerializer(data=data)
            if serializer.is_valid():
                try:
                    User.objects.get(mobile=mobile) #check whether aleady exists
                    return Response("Already registered user")
                except User.DoesNotExist:
                        password = make_password(data['password'])
                        serializer.save(user=True ,password=password)
                        mobile=serializer.data['mobile']
                        id=serializer.data['id']
                        old= User.objects.get(mobile= mobile)
                        old.username='hash0'+str(id)
                        old.save()
                        return Response("User registration is successfull",status=200)
            else:
                return Response(serializer.errors, status=400)


class LoginAPIView(APIView):
    """
        View for user Login
    """  
    permission_classes = [] #disables permission
    serializer_class = LoginSerializer
    def post(self,request):
        data=request.data
        email=data['email']
        password=data['password']
        try:
            use=User.objects.get(email=email)
            u=use.id
            user=use.user
            if(user==True):
                if user and check_password(password,use.password):
                    token, created = Token.objects.get_or_create(user=u)
                    result={
                        'id':u,
                        'token':token.key
                    }
                    return Response(result)
                return Response("Invalid password")
            return Response("Not a user")
        except User.DoesNotExist:
                return Response('User Does not exists')

