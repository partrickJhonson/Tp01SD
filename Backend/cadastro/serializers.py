from django.db.models import fields
from rest_framework import serializers
from  .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class RegisterSerilizer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68, min_length=6, write_only = True)

    class Meta:
        model = User
        fields = ['email','username','password']


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

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.object.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        filtered_user_by_email = User.object.get(email=email)
        #user = auth.authenticate(email=email, password=password)
        user=User.object.get(email=email, password=password)
        if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
            raise AuthenticationFailed(
                detail='Continue seu login usando:' + filtered_user_by_email[0].auth_provider)

        if not user:
            raise AuthenticationFailed('Dados invalidos, Tente Novamente')
        if not user.is_active:
            raise AuthenticationFailed('Usuário desativado, contate o admin'+user.username)
        if not user.is_verified:
            raise AuthenticationFailed('Email não foi verificado')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }

        return super().validate(attrs)
    