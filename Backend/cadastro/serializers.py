from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from  .models import User
from cadastro import models
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class RegisterSerilizer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68, min_length=6, write_only = True)

    class Meta:
        model = User
        fields = ['email','username','excluir','alterar','cadastrar','password']


        def validate(self, attrs):
            email = attrs.get('email','')
            username =attrs.get('username','')
            if not username.isalnum():
                raise serializers.ValidationError('Username contém caracteres alphanumericos')
            return attrs
        def create(self, validated_data):           
            return User.object.create_user(**validated_data)

class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']    

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(
        max_length=255, min_length=3, read_only=True)


    def get_tokens(self, obj):
        user = User.object.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['email', 'password', 'username','excluir','alterar','cadastrar','is_superuser', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        try:
            user = auth.authenticate(email=email, password=password)
            user=User.object.get(email=email, password=password)

            if not user:
                raise AuthenticationFailed('Dados invalidos, Tente Novamente')
            if not user.is_verified:
                raise AuthenticationFailed('Email não foi verificado, Acesso link enviado no email cadastrado ')                 
            if not user.is_active:
                raise AuthenticationFailed('Usuário:'+user.username+' desativado, contate o admin')
        except User.DoesNotExist:    
            try:
                user=User.object.get(email=email)
                if user:
                 raise AuthenticationFailed('Senha invalida')
            except: 
                 raise AuthenticationFailed('Dados Inválidos')
        return {
            'email':    user.email,
            'username': user.username,
            'tokens':   user.tokens,
            'excluir':  user.excluir,
            'alterar':  user.alterar,
            'cadastrar':user.cadastrar,
            'is_superuser': user.is_superuser
        }

        return super().validate(attrs)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

    