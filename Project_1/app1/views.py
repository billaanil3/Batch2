from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View

from django.views.decorators.csrf import csrf_exempt

from .models import Persons
from .models import NagStudent
# Create your views here.
def home(request):
    return render(request, "home.html")

def welcome_message(request):
    return HttpResponse("Welcome")


def auth_user_details(request):
    users = User.objects.all()
    return HttpResponse(users)

def even_numbers(request):
    evens = [i for i in range(10) if i%2==0]
    return HttpResponse(str(evens))

class PersonDetails(View):
    def get(self, request):
        persons = Persons.objects.all()
        return HttpResponse(persons)

    @csrf_exempt
    def post(self, request):
        # import pdb
        # pdb.set_trace()
        data = request.POST['data']

class NagStudentsDetails(View):
    def get(self, request):
        records = NagStudent.objects.all()
        if records:
            return HttpResponse(records)
        else:
            return HttpResponse("no records found")


def inputs(request):
    return render(request, "input.html")


def add_numbers(request):
    try:
        num1 = request.GET['n1']
        num2 = request.GET['n2']
        num3 = int(num1) + int(num2)
        return HttpResponse("<html><body bgcolor=cyan><h1> Sum of Two numbers:"+str(num3)+"</h1></body></html>")
    except ValueError:
        return HttpResponse("Invalid Input")        


def get_input(request):
    return render(request, "input1.html")

def post_input(request):
    return render(request, "input2.html")

def add_get_post_numbers(request):
    if request.method == "GET":
        try:
            num1 = request.GET['n1']
            num2 = request.GET['n2']
            num3 = int(num1) + int(num2)
            return HttpResponse("<html><body bgcolor=cyan><h1> Sum of Two numbers:"+str(num3)+"</h1></body></html>")
        except ValueError:
            return HttpResponse("Invalid Input")
    else:
        try:
            num1 = request.POST['n1']
            num2 = request.POST['n2']
            num3 = int(num1) * int(num2)
            return HttpResponse("<html><body bgcolor=cyan><h1> Multiplication of Two numbers:"+str(num3)+"</h1></body></html>")
        except ValueError:
            return HttpResponse("Invalid Input")


class AddGetPostNumbers(View):
    def get(self, request):
        num1 = request.GET['n1']
        num2 = request.GET['n2']
        num3 = int(num1) + int(num2)
        return HttpResponse("<html><body bgcolor=cyan><h1> Sum of Two numbers:"+str(num3)+"</h1></body></html>")
    def post(self, request):
        num1 = request.POST['n1']
        num2 = request.POST['n2']
        num3 = int(num1) * int(num2)
        return HttpResponse("<html><body bgcolor=cyan><h1> Multiplication of Two numbers:"+str(num3)+"</h1></body></html>")

class NagDetails(View):
    def get(self, request):
        records=NagStudent.objects.all()
        if records.len(NagStudent)>2:
            return HttpResponse(records(firstname+last_name))
        else:
            return HttpResponse("no records found")
    def post(self, request):
        records=NagStudent.objects.all()
        if records.len(NagStudent)<2:
            return HttpResponse(records(last_name+firstname))

def login(request):
    return render(request,"login.html")

def nag_student_register(request):
    return render(request,"nag_student_reg.html")
def save_nag_student(request):
    try:
        studentId = request.POST['st_id']
        FirstName = request.POST['first_name']
        Lastname =request.POST['last_name']
        subjectname = request.POST['subject_name']
        NagStudent.objects.create(st_id=studentId,last_name=Lastname,firstname= FirstName,sc_name=subjectname)
        NagStudent.objects.save()
        return HttpResponse("Nagtudent record created succesfully")
    except ValueError:
        return HttpResponse("Invalid Student details")
