from django.db import models
from uuid import uuid4


class Cadastro(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4,editable=False)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_pulicacao = models.IntegerField()
    estado = models.CharField(max_length=50)
    Npaginas = models.IntegerField()
    editora = models.CharField(max_length=255)
    criado_em = models.DateField(auto_now_add=True)


