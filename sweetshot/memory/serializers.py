from rest_framework import serializers

class MemorySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    date_created = serializers.DateField()
    club = serializers.CharField(max_length=100)
    course = serializers.CharField(max_length=5000)
    weather = serializers.CharField(max_length=500)
    memory_details = serializers.CharField(max_length=5000)
    date_amended = serializers.DateField()
    is_current = serializers.BooleanField()
    owner = serializers.CharField(max_length=100)