from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.generics import *
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    filter_backends = [SearchFilter, ]
    search_fields = ["title", ]

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
class CommentList(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    filter_backends = [SearchFilter, ]
    search_fields = ["matn", ]

class VideoLista(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers

class VideoView(RetrieveUpdateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
class VideoList(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
    filter_backends = [SearchFilter, ]
    search_fields = ["title", ]



