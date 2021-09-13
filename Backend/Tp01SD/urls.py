"""Tp01SD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path,include

from rest_framework import routers
from cadastro.api import viewsets as cadastroviewsetes,viewsets as  BuscarViewSet
from cadastro.views import  BuscarUser
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Cadastro de Metadados API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.ourapp.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="Teste License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

route = routers.DefaultRouter()
route.register(r'cadastro',cadastroviewsetes.CadastroViewSet, basename="Cadastro")
route.register(r'buscar',BuscarViewSet.BuscarViewSet, basename="Buscar")
route.register(r'buscaruser',BuscarUser, basename="Buscar")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include(route.urls)),
    path('auth/',include('cadastro.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')  
]
