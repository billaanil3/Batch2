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
    path('odds/', views.odd_numbers),
    path('wish/', views.EmployeeDetials.as_view()),
    path('persons/', views.PersonDetails.as_view()),
    path('NagStudent/', views.NagStudentsDetails.as_view()),
    path('inputss/', views.inputing, name = 'inputss'),
    path('div/', views.division_numbers,name = 'div'),
    path('take input/', views.take_input, name = 'take input'),
    path('give input/', views.give_input,name = 'give input'),
    path('div_get_post/', views.div_get_post_number, name = 'add_get_post_numbers'),
    path('emp_login/', views.emp_login, name = 'emp_login'),
    path('register/', views.emp_register, name = 'register'),
    path('save_employee_register/', views.save_employee_register, name="emp_records"),
    path('DivGetPostNumbers/', views.DivGetPostNumber.as_view(),name='DivGetPostNumbers'),
    path('input/', views.inputs, name="input"),
    path('add/', views.add_numbers, name="add"),
    path('get_input/', views.get_input, name="get_input"),
    path('post_input/', views.post_input, name="post_input"),
    path('add_get_post/', views.add_get_post_numbers, name="add_get_post_numbers"),
    path('AddGetPostNumbers/', views.AddGetPostNumbers.as_view(), name="AddGetPostNumbers"),
    path('NagDetails/', views.NagDetails.as_view(), name="NagDetails"),
    path('nag_student_register/', views.nag_student_register, name="register page"),
    path('save_nag_student/', views.save_nag_student, name="records page"),
    path('save_nag_student_via_forms/', views.save_nag_student_via_forms, name="save_nag_student_via_forms"),
    path('save_nag_student_via_model_forms/', views.save_nag_student_via_model_forms, name="save_nag_student_via_model_forms"),
    path('display/', views.dipaly_students, name="dipaly_students"),
    path('save_employee_via_forms/', views.save_employee_via_forms, name="save_employee_via_forms"),
    path('save_employee_via_model_forms', views.save_employee_via_model_forms, name="save_employee_via_model_forms"),
    path('display/',views.display_employees, name="display employees")
    
]
