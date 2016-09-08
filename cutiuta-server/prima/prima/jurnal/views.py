#from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from prima.jurnal.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """Utilizatorii pot fi pacienti sau medici.Deocamdata ne jucăm doar cu utilizatorii ce sunt pacienți si doar un superuser.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """ API endpoin ca sa vezi sau editezi grupurile"""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
