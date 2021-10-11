from rest_framework import serializers
from .models import CustomUser
from django.utils import timezone

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only=True)
    terms = serializers.BooleanField(default=True, write_only=True)
    created_on = serializers.DateField(default=timezone.now, write_only=True)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class CustomUserDetailSerializer(CustomUserSerializer):

    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        return instance