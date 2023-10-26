from django.shortcuts import render
from .models import Post, PostComment, PostLike, CommentLike
from .serializers import PostSerializer, PostLikeSerializer, CommentSerializer, CommentLikeSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from shared.custom_pegination import CustomPagination
# Create your views here.


class PostListApiView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny, ]
    pagination_class = CustomPagination

    def get_queryset(self):
        return Post.objects.all()
