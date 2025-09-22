from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from helloworld.serializers import BlogSerializer
from helloworld.models import Post
from rest_framework.permissions import IsAuthenticated
from helloworld.permissions import IsOwnerOrReadOnly
from rest_framework import filters
from helloworld.filters import BlogFilter
from django_filters.rest_framework import DjangoFilterBackend

class HelloWorldView(APIView):
    def get(self, request):
        return Response({'message': 'Hello, World!'})

class BlogView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BlogFilter
    ordering_fields = ['id']
    search_fields = ['title', 'content']

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)