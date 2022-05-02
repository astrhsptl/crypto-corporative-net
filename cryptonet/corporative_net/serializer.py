from rest_framework import serializers

from .models import Orders

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('__all__')