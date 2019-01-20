from rest_framework import serializers

from .models import Point


class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ('x', 'y')
