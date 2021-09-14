from django.shortcuts import render
from rest_framework import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Memory
from .serializers import MemorySerializer

class MemoryList(APIView):

    def get (self, request):
        memory = Memory.objects.all()
        serializer = MemorySerializer(memory, many=True)
        return Response(serializer.data)
        