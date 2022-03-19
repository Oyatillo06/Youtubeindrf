from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *
class AccountView(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers

class AccountList(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers
    filter_backends = [SearchFilter, ]
    search_fields = ["first_name", ]

