from rest_framework import viewsets
from cadastro.api import serializer
from cadastro import models
from django_filters.rest_framework import DjangoFilterBackend

class CadastroViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.CadastroSerializer
    queryset = models.Cadastro.objects.all()

class BuscarViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.CadastroSerializer
    queryset = models.Cadastro.objects.all()
    filter_backends =[DjangoFilterBackend]
    filterset_fields= ['titulo','Npaginas','autor','ano_pulicacao','id_identificador']