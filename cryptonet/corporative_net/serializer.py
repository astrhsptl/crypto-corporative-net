from rest_framework import serializers

from .models import Orders, Clients, Posts, Workers

class AllOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('__all__')

class AllClientsSerializer(serializers.ModelSerializer):
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