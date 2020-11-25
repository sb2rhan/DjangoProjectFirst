from rest_framework import serializers, viewsets

from .models import Todo

"""
    Serializers convert QueryDictionary data to JSON and vice versa
"""
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['description', 'status', 'id']
