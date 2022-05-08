from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Orders, Clients, Workers, Posts, Prices
from .serializer import OrdersSerializer, ClientsSerializer, PostsSerializer, WorkersSerializer
from .serializer import ListOrdersSerializer, ListWorkersSerilizer, PricesSerializer

from .buisneslogic.parser import get_and_write_all_prices
# Create your views here.

class PricesAPIView(APIView):
    def get(self, request):
        print(get_and_write_all_prices())
        lst = Prices.objects.raw(
        'select * from prices order by id desc limit 1;'
        )
        return Response({'prices': PricesSerializer(lst, many=True).data})

#list classes
class OrdersListAPIView(ListAPIView):
    queryset = Orders.objects.raw(
    "select o.id, o.title, o.discription, cnc.name, cnw.lastname, o.client_sum, o.status from orders as o join corporative_net_clients as cnc on cnc.id=o.client_id_id join corporative_net_workers as cnw on cnw.id=o.executor_id_id;"
    )
    serializer_class = ListOrdersSerializer
    permission_classes = (IsAdminUser,)

class ClientsListAPIView(ListAPIView):
    queryset = Clients.objects.raw(
        'select * from corporative_net_clients;'
    )
    serializer_class = ClientsSerializer
    permission_classes = (IsAdminUser,)

class WorkersListAPIView(ListAPIView):
    queryset = Workers.objects.raw(
        'select cnw.*, p.title from corporative_net_workers as cnw join posts as p on p.id=cnw.post_id_id;'
)     
    serializer_class = ListWorkersSerilizer
    permission_classes = (IsAdminUser,)

class PostsListAPIView(ListAPIView):
    queryset = Posts.objects.raw(
        'select * from posts;'
)
    serializer_class = PostsSerializer
    permission_classes = (IsAdminUser,)

#retrieve classes
class OrderRetrieveAPIView(RetrieveAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (IsAdminUser,)

class WorkersRetrieveAPIView(RetrieveAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer
    permission_classes = (IsAdminUser,)

class ClientsRetrieveAPIView(RetrieveAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    permission_classes = (IsAdminUser,)

class PostsRetrieveAPIView(RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (IsAdminUser,)