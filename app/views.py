from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from rest_framework.generics import CreateAPIView,ListAPIView
from .models import CustomUser
from .serializers import UserSerializer


# create a user
class CreateUser(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


# list all users
class ListUser(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
