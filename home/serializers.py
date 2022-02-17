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
    user = UserSerializer()
    class Meta :
        model = Customer
        fields = ["profile_number","user"]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(
            first_name = user_data['first_name'],
            last_name = user_data['last_name'],
            email = user_data['email'],
            mobile_no = user_data['mobile_no']
        )
        
        # import pdb; pdb.set_trace()
        print(user_data)
        customer = Customer.objects.create(
            profile_number = validated_data['profile_number'],
            user= user
        )

        return customer   