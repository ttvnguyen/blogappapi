from django.shortcuts import render

# Create your views here.
from .models import Blog
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Blog.objects.all()
    # The serializer class for serializing output
    serializer_class = BlogSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]