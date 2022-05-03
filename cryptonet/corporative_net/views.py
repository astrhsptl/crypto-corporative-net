from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView 
from rest_framework.viewsets import ModelViewSet

from .models import Orders, Clients, Workers, Posts
from .serializer import OrdersSerializer, ClientsSerializer, PostsSerializer, WorkersSerializer
from .serializer import TestSerializer
# Create your views here.

class TestViewSet(ModelViewSet):
    queryset = Orders.objects.raw(
    "select o.id, o.title, o.discription, cnc.name, o.client_sum, o.status from orders as o join corporative_net_clients as cnc on cnc.id=o.executor_id_id;")
    serializer_class = TestSerializer

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

def first(request):
    print(f'{Orders.objects.raw("select o.*, cnc.name from orders as o join corporative_net_clients as cnc on cnc.id=o.id;")}')
    return HttpResponse(f'<h1>{Clients.objects.all()}</h1>')