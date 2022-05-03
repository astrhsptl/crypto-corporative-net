from django.urls import path

from corporative_net.views import OrdersListAPIView, ClientsListAPIView, PostsListAPIView, WorkersListAPIView
urlpatterns = [
    path('orders/', OrdersListAPIView.as_view()),
    path('clients/', ClientsListAPIView.as_view()),
    path('posts/', PostsListAPIView.as_view()),
    path('workers/', WorkersListAPIView.as_view())
]
