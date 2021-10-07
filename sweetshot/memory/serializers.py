from rest_framework import serializers
from .models import Memory

class MemorySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    date_created = serializers.DateField()
    club = serializers.CharField(max_length=100)
    course = serializers.CharField(max_length=5000)
    shot_date = serializers.DateField()
    weather = serializers.CharField(max_length=500)
    memory_details = serializers.CharField(max_length=5000)
    date_amended = serializers.DateField()
    is_current = serializers.BooleanField()
    owner = serializers.ReadOnlyField(source='owner.id')

    def create(self, validated_data):
        return Memory.objects.create(**validated_data)

class MemoryDetailSerializer(MemorySerializer):

    def update (self, instance, validated_data):
        instance.club = validated_data.get('club', instance.club)
        instance.course = validated_data.get('course', instance.course)
        instance.shot_date = validated_data.get('shot_date', instance.shot_date)
        instance.weather = validated_data.get('weather', instance.weather)
        instance.memory_details = validated_data.get('memory_details', validated_data.memory_details)
        instance.date_amended = validated_data.get('date_amended', instance.date_amended)
        instance.is_current = validated_data.get('is_current', instance.is_current)
        instance.save()
        return instance