# from django.urls import reverse
# from rest_framework.response import Response
# import jwt
# from rest_framework import status
# from .models import Profile

# class JWTAuthmiddleware:
#     def __init__(self,get_response):
#         self.get_response = get_response
#         self.excluded_paths = [reverse('login'),reverse('register')]

#     def __call__(self,request):
#         if request.path in self.excluded_paths or request.path.startswith('/admin/'):
#             return self.get_response(request)

#         token= request.COOKIES.get('jwt')
#         payload=jwt.decode(token,'cap1.4b',algorithms=['HS256'])
#         profile = Profile.objects.filter(user=payload['id']).first()
#         if profile.user_type != 'author' and profile.user_type != 'admin':
#             return Response({'message':"Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
#         request.author= profile
#         response=self.get_response(request)
#         return response