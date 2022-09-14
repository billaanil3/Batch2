"""Project_1 URL Configuration

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
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="home"),
    path('welcome/', views.welcome_message),
    path('auth_users/', views.auth_user_details),
    path('evens/', views.even_numbers),
    path('persons/', views.PersonDetails.as_view()),
    path('NagStudent/', views.NagStudentsDetails.as_view()),
    path('input/', views.inputs, name="input"),
    path('add/', views.add_numbers, name="add"),
    path('get_input/', views.get_input, name="get_input"),
    path('post_input/', views.post_input, name="post_input"),
    path('add_get_post/', views.add_get_post_numbers, name="add_get_post_numbers"),
    path('AddGetPostNumbers/', views.AddGetPostNumbers.as_view(), name="AddGetPostNumbers")
]
