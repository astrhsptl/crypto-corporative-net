from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView

from .models import Orders
from .serializer import TestSerializer
# Create your views here.

def first(request):
    return HttpResponse('succesful')

class TestAPIView(ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = TestSerializer