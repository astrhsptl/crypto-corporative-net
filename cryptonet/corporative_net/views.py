from django.http import HttpResponse
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView 

from .models import Orders, Clients, Workers, Posts
from .serializer import OrdersSerializer, ClientsSerializer, PostsSerializer, WorkersSerializer

# Create your views here.

#list classes
class OrdersListAPIView(ListAPIView):
    queryset = Orders.objects.raw(
        'select * from orders order by client_sum desc;'
)
    serializer_class = OrdersSerializer

class ClientsListAPIView(ListAPIView):
    queryset = Clients.objects.raw(
        'select * from corporative_net_clients;'
    )
    serializer_class = ClientsSerializer

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

#retrieve classes
class OrderRetrieveAPIView(RetrieveUpdateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class WorkersRetrieveAPIView(RetrieveUpdateAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer

class ClientsRetrieveAPIView(RetrieveUpdateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

class PostsRetrieveAPIView(RetrieveUpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer