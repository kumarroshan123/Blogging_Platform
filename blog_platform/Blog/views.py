from django.shortcuts import render
from .models import Profile, Post, Comment
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
import jwt,datetime
from django.contrib.auth import authenticate,login
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

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()

        if user is None or not user.check_password(password):
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)
        payload={
            'id':user.id,
            'exp':datetime.datetime.now(datetime.UTC)+datetime.timedelta(minutes=60),
            'iat':datetime.datetime.now(datetime.UTC)

        }
        token=jwt.encode(payload,'cap1.4b',algorithm='HS256')
        response=Response()
        response.data={'message': 'login successful' , 'token':token}
        response.status = status.HTTP_200_OK
        response.set_cookie(
            key='jwt',
            value=token,
            httponly=False,
            samesite=None,
            secure=None
        )
        return response
        # return Response({'message':'Login successful','token':token}, status=status.HTTP_200_OK)