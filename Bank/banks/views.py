from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

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

