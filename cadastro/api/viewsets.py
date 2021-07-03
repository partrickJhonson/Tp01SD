from rest_framework import viewsets
from cadastro.api import serializer
from cadastro import models

class CadastroViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.CadastroSerializer
    queryset = models.Cadastro.objects.all()