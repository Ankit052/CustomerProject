from asyncore import read
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import User,Customer


class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ["first_name","last_name","email","mobile_no"]

class CustomerSerializer(serializers.ModelSerializer):
    class Meta :
        model = Customer
        fields = ["profile_number","user"]