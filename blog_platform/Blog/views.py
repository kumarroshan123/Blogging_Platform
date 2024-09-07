from django.shortcuts import render
from .models import Profile, Post, Comment
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            profile = Profile(user=user, user_type=request.data.get('user_type', 'reader'))
            profile.save()
            return Response({'message': "Signup Successful", 'user_details': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message': "Invalid Credentials"}, status=status.HTTP_406_NOT_ACCEPTABLE)
