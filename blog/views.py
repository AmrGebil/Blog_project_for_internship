from django.shortcuts import render
from rest_framework import generics
from .models import Tag
from .seializer import TagSerializer
# Create your views here.



class TagListView(generics.ListAPIView):
    """
    to list Tages with id,name
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer