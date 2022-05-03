from rest_framework import serializers

from .models import Orders, Clients, Posts, Workers

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('__all__')

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('__all__')

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('__all__')
    
class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = ('__all__')
        
class TestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    discription = serializers.CharField(max_length=511)
    executor_id = serializers.CharField()
    client_id = serializers.CharField()
    client_sum = serializers.IntegerField()
    status = serializers.CharField(max_length=255)
    create_date = serializers.DateField(read_only=True)
    name = serializers.CharField(max_length=255)