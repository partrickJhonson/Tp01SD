from threading import current_thread
from django.http import response
from .serializers import RegisterSerilizer,EmailVerificationSerializer,LoginSerializer,UserSerializer
from rest_framework import generics,status,views,viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import  Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import Settings, settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from cadastro import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class RegisterView(generics.GenericAPIView):
    serializer_class=RegisterSerilizer
    def post (self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data =serializer.data
        user = User.object.get(email=user_data['email'])

        token = RefreshToken.for_user(user).access_token
        
        current_site = get_current_site(request).domain
        relativeLink = reverse('VerifyEmail')
        absurl = 'http://localhost:8080/VerifiEmail/'+str(token)
        email_body = 'Olá '+user.username + \
            ' Use o link para verificar seu  email e liberar acesso ao nosso sistema \n' + absurl
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verificação de Emaail'}

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)

class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
            user = User.object.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.is_active   = True
                user.save()
            return Response({'email': 'Usuário Ativado com Secesso'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Token Expirado'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': ' token Inválido'}, status=status.HTTP_400_BAD_REQUEST)
    
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BuscarUser(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = models.User.object.all()
    filter_backends =[DjangoFilterBackend,SearchFilter]
    filterset_fields= ['username']
    search_fields =   ['username']
    