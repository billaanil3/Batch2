from django.urls import path
from CryceTruly import views

urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name='register-user'),
    path('login', views.LoginAPIView.as_view(), name='login-user'),
    path('user', views.AuthUserAPIView.as_view(), name='authenticate-user')
]