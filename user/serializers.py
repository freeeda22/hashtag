from rest_framework import serializers
from .models import *

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ('email','password' )
