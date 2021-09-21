from django.shortcuts import render
from django.http import Http404
from rest_framework import serializers, status

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Memory
from .serializers import MemorySerializer

class MemoryList(APIView):

    def get (self, request):
        memory = Memory.objects.all()
        serializer = MemorySerializer(memory, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MemorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class MemoryDetail(APIView):

    def get_object(self, pk):
        try:
            return Memory.objects.get(pk=pk)
        except Memory.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        memory = self.get_object(pk)
        serializer = MemorySerializer(memory)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )