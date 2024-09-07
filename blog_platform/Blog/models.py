from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user_roles = (('reader', 'Reader'), ('author', 'Author'), ('admin', 'Admin'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=user_roles, default='reader')

    def __str__(self) -> str:
        return f'{self.user}-{self.user_type}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title}-{self.author}'   