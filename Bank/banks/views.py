from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render

from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import JSONParser

from .models import Bank, Branch, Client, Account
from .serializers import (UserSerializer, GroupSerializer, BankSerializer,
                          AccountSerializer, ClientSerializer, BranchSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class BankViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows banks to be viewed or edited.
    """
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [permissions.IsAuthenticated]

class BranchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows banks to be viewed or edited.
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows banks to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows banks to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def bank_list(request: HttpRequest) -> JsonResponse:
    """
    List all banks or create a new bank
    :param request:
    :return:
    """
    if request.method == 'GET':
        banks = Bank.objects.all()
        ser = BankSerializer(banks, many=True)
        return JsonResponse(ser.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser = BankSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status=400)

@csrf_exempt
def bank_detail(request, pk):
    """
    Retrieve, update or delete a bank.
    """
    try:
        bank = Bank.objects.get(pk=pk)
    except Bank.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BankSerializer(bank)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BankSerializer(bank, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        bank.delete()
        return HttpResponse(status=204)
