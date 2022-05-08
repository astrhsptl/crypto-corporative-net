from rest_framework import serializers

from .models import Orders, Clients, Posts, Workers, Prices

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
        
class ListOrdersSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    discription = serializers.CharField(max_length=511)
    name = serializers.CharField(max_length=255)
    lastname = serializers.CharField(max_length=255,)
    client_sum = serializers.IntegerField()
    status = serializers.CharField(max_length=255)
    create_date = serializers.DateField(read_only=True)

class ListWorkersSerilizer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    lastname = serializers.CharField(max_length=511)
    title = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=255,)

class PricesSerializer(serializers.Serializer):
    crypt_one = serializers.CharField(max_length=255)
    price_one = serializers.IntegerField()
    crypt_two = serializers.CharField(max_length=255)
    price_two = serializers.IntegerField()