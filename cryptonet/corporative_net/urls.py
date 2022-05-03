from django.urls import path, include
from rest_framework import routers

from corporative_net.views import OrdersListAPIView, ClientsListAPIView, PostsListAPIView, WorkersListAPIView
from corporative_net.views import OrderRetrieveAPIView, WorkersRetrieveAPIView, ClientsRetrieveAPIView, PostsRetrieveAPIView
from corporative_net.views import TestViewSet

router = routers.SimpleRouter()
router.register(r'qwerty', TestViewSet, basename='qwerty')

urlpatterns = [
    path('orders/', OrdersListAPIView.as_view()),
    path('clients/', ClientsListAPIView.as_view()),
    path('posts/', PostsListAPIView.as_view()),
    path('workers/', WorkersListAPIView.as_view()),

    path('orders/<int:pk>', OrderRetrieveAPIView.as_view()),
    path('clients/<int:pk>', ClientsRetrieveAPIView.as_view()),
    path('posts/<int:pk>', PostsRetrieveAPIView.as_view()),
    path('workers/<int:pk>', WorkersRetrieveAPIView.as_view()),

    path('test/', include(router.urls))
]
