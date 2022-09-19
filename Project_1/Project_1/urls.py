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
    path('login/', views.login, name="login"),
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
    path('AddGetPostNumbers/', views.AddGetPostNumbers.as_view(), name="AddGetPostNumbers"),
    #path('NagDetails/', views.NagDetails.as_view(), name="NagDetails"),
    path('nag_student_register/', views.nag_student_register, name="register page"),
    path('save_nag_student/', views.save_nag_student, name="records page"),
    path('save_nag_student_via_forms/', views.save_nag_student_via_forms, name="save_nag_student_via_forms"),
    path('save_nag_student_via_model_forms/', views.save_nag_student_via_model_forms, name="save_nag_student_via_model_forms"),
    path('display/', views.dipaly_students, name="dipaly_students"),
    path('breakfast_details/', views.get_breakfast_details, name="get_breakfast_details"),
    path('cookie_example/', views.cookie_example, name="cookie_example"),
    path('add_by_cookie/', views.add_by_cookie, name="add_by_cookie"),
    path('display_by_cookie/', views.display_by_cookie, name="display_by_cookie"),
    path('session_example/', views.session_example, name="session_example"),
    path('add_by_session/', views.add_by_session, name="add_by_session"),
    path('display_by_session/', views.display_by_session, name="display_by_session"),
    path('NagTeacherDetails/', views.NagTeacherDetails.as_view(), name="TeacherDetails"),
    path('TeacherDetailsAsTable/', views.TeacherDetailsAsTable, name="TeacherDetailsAsTable"),
]
