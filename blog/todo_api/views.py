from django.shortcuts import render
from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSerializer

"""
    Viewset is needed to get a GUI panel at rest api's url
"""
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
