from django.contrib.auth.models import User, Group
from prima.jurnal.models import Pacient
from rest_framework import serializers


class PacientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pacient
        fields = ('url', 'user','unitate_masura', 'valoare_max', 'valoare_min', 'perioada_raportare', 'categorie', 'telefon')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')



