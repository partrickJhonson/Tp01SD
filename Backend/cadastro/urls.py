from django.urls import path
from django.urls.converters import register_converter
from django.urls import path
from .views import RegisterView,VerifyEmail,LoginAPIView



urlpatterns =[
    path('register/', RegisterView.as_view(),name="register"),
    path('emailverify/', VerifyEmail.as_view(),name="VerifyEmail"),    
    path('Login/', LoginAPIView.as_view(),name="login"), 
] 
