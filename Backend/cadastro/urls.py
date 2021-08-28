from django.urls import path
from django.urls.converters import register_converter
from django.urls import path
from .views import RegisterView

urlpatterns =[
    path('register/', RegisterView.as_view(),name="register")
]
