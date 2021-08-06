from rest_framework.views import viewsets
from . import models
from . import serializer
from Backend import cadastro

class Cadastro_Buscar(viewsets.ModelViewSet):
    queryset = models.cadastro.objects.all()
    serializer = serializer(cadastro.data)
    