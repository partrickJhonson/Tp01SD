from django.db import models
from uuid import UUID, uuid4
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin, User, UserManager)
from rest_framework_simplejwt.tokens import RefreshToken

AUTH_PROVIDERS = {'email': 'email'}

class Usuario(BaseUserManager):
    def create_user(self,username,email,password=None):

        if username is None:
            raise TypeError('Nome não pode ser nulo')
        if email is None:
            raise TypeError('Email não pode ser nulo')
        
        user=self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,username,email,password=None):
    
        if password is None:
            raise TypeError('Senha não pode ser nulo')
        user=self.create_user(username,email,password)        
        user.is_superuser=True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=255, unique=True,db_index = True)
    email = models.CharField(max_length=255, unique=True,db_index = True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['username']


    object = UserManager()


    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        } 


class Cadastro(models.Model):
    #Geral
    id_identificador = models.UUIDField(primary_key=True, default=uuid4,editable=False)
    titulo = models.CharField(max_length=20)
    catalogo = models.CharField(max_length=20,null=True,blank=True)
    EntradaNoCatalogo = models.DateField(auto_now_add=True)
    Lingua = models.CharField(max_length=20,null=True,blank=True)
    Descrisao = models.CharField(max_length=20,null=True,blank=True)
    palavrachave= models.CharField(max_length=20,null=True,blank=True)
    Corbertura = models.CharField(max_length=20,null=True,blank=True)
    Estrtura =  models.CharField(max_length=20,null=True,blank=True)
    NiveldeAgregacao = models.IntegerField(default=0,null=True,blank=True)
#Ciclo de Vida
    Versao = models.CharField(max_length=20,null=True,blank=True)
    Status = models.CharField(max_length=10,null=True,blank=True)
    ContribuinteFuncao = models.CharField(max_length=20,null=True,blank=True)
    ContribuinteEntidadae = models.CharField(max_length=20,null=True,blank=True)
    ContribuinteData = models.CharField(max_length=20,null=True,blank=True)
#Meta-Metadados
    identificador = models.CharField(max_length=20,null=True,blank=True)
    catalogoMeta = models.CharField(max_length=20,null=True,blank=True)
    catalogoMetaEntrada = models.CharField(max_length=20,null=True,blank=True)
    catalogoMetaData = models.CharField(max_length=20,null=True,blank=True)
    EsquemaMeta = models.CharField(max_length=20,null=True,blank=True)
    idiomameta = models.CharField(max_length=20,null=True,blank=True)
#Tecnico
    formato = models.CharField(max_length=20,null=True,blank=True)
    tamanho = models.CharField(max_length=20,null=True,blank=True)
    localizacao = models.CharField(max_length=20,null=True,blank=True)
    requisitoTipo = models.CharField(max_length=20,null=True,blank=True)
    requisitoNome = models.CharField(max_length=20,null=True,blank=True)
    Observacao= models.CharField(max_length=20,null=True,blank=True)
    outrosRequitos = models.CharField(max_length=20,null=True,blank=True)
    duracao = models.CharField(max_length=20,null=True,blank=True)
#Educaional
    tipodeinteratividade = models.CharField(max_length=20,null=True,blank=True)
    tipodeRecursodeAprendizagem = models.CharField(max_length=20,null=True,blank=True)
    niveldeinteratividade = models.CharField(max_length=20,null=True,blank=True)
    densidadesemantica = models.CharField(max_length=20,null=True,blank=True)
    funcaodousuariofinalpretendido = models.CharField(max_length=20,null=True,blank=True)
    contexto = models.CharField(max_length=20,null=True,blank=True)
    faixaEtaria = models.CharField(max_length=20,null=True,blank=True)
    dificuldade = models.CharField(max_length=20,null=True,blank=True)
    TempodeAprendizagem = models.CharField(max_length=20,null=True,blank=True)
    DescrisaoEducacional = models.CharField(max_length=20,null=True,blank=True)
    idioma = models.CharField(max_length=20,null=True,blank=True)
#Direitos
    custo = models.CharField(max_length=20,null=True,blank=True)
    DireitosautoraisRestricoes = models.CharField(max_length=20,null=True,blank=True)
    DescrisaoDireitos = models.CharField(max_length=20,null=True,blank=True)
#Relacao
    tipoRelacao = models.CharField(max_length=20,null=True,blank=True)
    recursoRelacao =models.CharField(max_length=20,null=True,blank=True)
#Anotação
    pessoaAnotacao = models.CharField(max_length=20,null=True,blank=True)
    dataanotacao = models.CharField(max_length=20,null=True,blank=True)
    descrisaoanotacao = models.CharField(max_length=20,null=True,blank=True)
#Clasificao
    closificacaoObjetivo = models.CharField(max_length=20,null=True,blank=True)
    taxon = models.CharField(max_length=20,null=True,blank=True)
    taxonFonte = models.CharField(max_length=20,null=True,blank=True)
    taxonId = models.CharField(max_length=20,null=True,blank=True)
    taxonEntrada = models.CharField(max_length=20,null=True,blank=True)
    classificacaoDescrisao = models.CharField(max_length=20,null=True,blank=True)
    PalavraPasseClassificacao = models.CharField(max_length=20,null=True,blank=True)
    autor = models.CharField(max_length=20,null=True,blank=True)
    ano_pulicacao = models.IntegerField(default=2020)
    estado = models.CharField(max_length=20,null=True,blank=True)
    Npaginas = models.IntegerField(default=0,null=True,blank=True)
    editora = models.CharField(max_length=20,null=True,blank=True)

