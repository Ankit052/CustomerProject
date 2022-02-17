from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from .models import *

# Create your views here.

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
