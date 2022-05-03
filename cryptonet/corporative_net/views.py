from django.http import HttpResponse
from rest_framework.generics import ListAPIView

from .models import Orders, Clients, Workers, Posts
from .serializer import AllOrdersSerializer, AllClientsSerializer, PostsSerializer, WorkersSerializer

# Create your views here.

class OrdersListAPIView(ListAPIView):
    queryset = Orders.objects.raw(
        'select * from orders order by client_sum desc;'
)
    serializer_class = AllOrdersSerializer

class ClientsListAPIView(ListAPIView):
    queryset = Clients.objects.raw(
        'select * from corporative_net_clients;'
    )
    serializer_class = AllClientsSerializer

    #'select o.*, cnc.name from orders as o join corporative_net_clients as cnc on cnc.id=o.id;'

class WorkersListAPIView(ListAPIView):
    queryset = Workers.objects.raw(
        'select * from corporative_net_workers;'
)     
    serializer_class = WorkersSerializer

class PostsListAPIView(ListAPIView):
    queryset = Posts.objects.raw(
        'select * from posts;'
)
    serializer_class = PostsSerializer
