from django.urls import path 
from .views import RegisterView, LoginView, PostView, PostListView, CommentView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('posts/', PostView.as_view(), name='create_post'),
    path('posts/all/', PostListView.as_view(), name='post_list'),
    path('posts/<int:post_id>/comments/', CommentView.as_view(), name='add_comment'),
]
