from rest_framework import serializers
from .models import (Food)

class FoodSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=128)
    created = serializers.DateTimeField(read_only=True)
    hotel_id = serializers.IntegerField(source='hotel.id')

    def create(self, validated_data):
        """
        Create and return a new `Food` instance, given the validated data.
        """
        pk = validated_data.get("hotel").get("id")
        name = validated_data.get("name")
        return Food.objects.create(name=name)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Food` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
