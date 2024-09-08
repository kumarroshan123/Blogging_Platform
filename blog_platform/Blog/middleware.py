from django.urls import reverse
from rest_framework.response import Response

class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.excluded_paths = [reverse('login'), reverse('register'), reverse('reset_password')]

        def __call__(self, request):
            if request.path in self.excluded_paths or request.path.startswith('/admin/'):
                return self.get_response(request)