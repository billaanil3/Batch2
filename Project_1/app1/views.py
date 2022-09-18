from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View

from django.views.decorators.csrf import csrf_exempt

from .models import Persons
from .models import NagStudent
from .models import Employee
from .forms import NagStudentForm, NagStudentModelForm,EmployeeForm,EmployeeModelForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def welcome_message(request):
    return HttpResponse("Welcome")

def swagatham(request):
    return  HttpResponse('welcome to our world')


def odd_numbers(request):
    odds = [a for a in range(60) if a%2 != 0]
    return HttpResponse(str(odds))

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


class EmployeeDetials(View):
    def get(self,request):
        employes = Employee.objects.all()
        return  HttpResponse(employes)

    @csrf_exempt
    def post(self,request):
        data = request.POST('data')


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


def inputing(request):
    return render(request,"input3.html")


def division_numbers(request):
    try:
        s1 = request.GET['n1']
        s2 = request.GET['n2']
        s3 = int(s1) / int(s2)
        return HttpResponse("<html><body bgcolor=cyan><h1> Division of Two numbers:"+str(s3)+"</h1></body></html>")
    except ZeroDivisionError:
        return HttpResponse("s2 value must be < or > 0 but not equal to 0")


def take_input(request):
    return render(request, "input4.html")


def div_get_post_number(request):
    if request.method == "GET":
        try:
            s1 = request.GET['n1']
            s2 = request.GET['n2']
            s3 = int(s1) / int(s2)
            return HttpResponse(
                "<html><body bgcolor=cyan><h1> Division of Two numbers:" + str(s3) + "</h1></body></html>")
        except ZeroDivisionError:
            return HttpResponse("give another value to s2")
    else:
        try:
            s1 = request.POST['n1']
            s2 = request.POST['n2']
            s3 = int(s1) // int(s2)
            return HttpResponse("<html><body bgcolor=cyan><h1>Perfect division of Two numbers:" + str(s3) + "</h1></body></html>")
        except ZeroDivisionError:
            return HttpResponse("give another value to s2")


def give_input(request):
    return render(request, "input5.html")


class DivGetPostNumber(View):
    def get(self,request):
        s1 = request.GET['n1']
        s2 = request.GET['n2']
        s3 = int(s1) / int(s2)
        return HttpResponse("<html><body bgcolor=cyan><h1> Division of Two numbers:" + str(s3) + "</h1></body></html>")
    def post(self,request):
        s1 = request.POST['n1']
        s2 = request.POST['n2']
        s3 = int(s1) // int(s2)
        return HttpResponse("<html><body bgcolor=cyan><h1>Perfect division of Two numbers:" + str(s3) + "</h1></body></html>")



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

@csrf_exempt
def save_nag_student(request):
    try:
        studentId = request.POST.get('st_id')
        FirstName = request.POST.get('first_name')
        Lastname =request.POST.get('last_name')
        subjectname = request.POST.get('subject_name')
        NagStudent.objects.create(st_id=studentId,last_name=Lastname,firstname= FirstName,sc_name=subjectname)
        return HttpResponse("Nagtudent record created succesfully")
    except ValueError:
        return HttpResponse("Invalid Student details")


def emp_login(request):
    return render(request,'emply_login.html')


def emp_register(request):
    return render(request, 'employee_reg.html')

@csrf_exempt
def save_employee_register(request):
    try:
        EmployeeId = request.POST.get('em_id')
        EmpName = request.POST.get('name')
        EmpInitial = request.POST.get('initial')
        CmpName = request.POST.get('cmp_name')
        area = request.POST.get('e_area')
        Employee.objects.create(Emp_id = EmployeeId,Name=EmpName,Initial=EmpInitial,CompanyName=CmpName,Area=area)
        return HttpResponse("employee record created")
    except ValueError:
        return HttpResponse("invalid employee detials")

def save_nag_student_via_forms(request):
    form = NagStudentForm(request.POST)
    if form.is_valid():
        student = NagStudent(st_id=form.cleaned_data['sid'],
                             last_name=form.cleaned_data['lastName'],
                             firstname=form.cleaned_data['firstName'],
                             sc_name=form.cleaned_data['subjectName']
                            )
        student.save()
        return HttpResponse("Nag Student data inserted successfully!!!!")
    return render(request, "save_nag_student_via_forms.html", {'myform': form})

def save_nag_student_via_model_forms(request):
    if request.method == "POST":
        form = NagStudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "links.html")
    else:
        form = NagStudentModelForm()
    return render(request, "data.html", {'myform': form})


def save_employee_via_forms(request):
    form = EmployeeForm(request.POST)
    if form.is_valid():
        employee = Employee(EmpId=form.cleaned_data['eid'],
                             Name=form.cleaned_data['eName'],
                             Initial=form.cleaned_data['eInitial'],
                             CompanyName=form.cleaned_data['cName'],
                             Area=form.cleaned_data['area']
                            )
        employee.save()
        return HttpResponse("employee data inserted successfully!!!!")
    return render(request, "save_employee_via_forms.html", {'myform': form})

def save_employee_via_model_forms(request):
    if request.method == "POST":
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "links.html")
    else:
        form = EmployeeModelForm()
    return render(request, "data.html", {'myform': form})


def dipaly_students(request):
    students = NagStudent.objects.all()
    print("================================", students)
    return render(request, "display.html", {"records": students})

def display_employees(request):
    employes = Employee.objects.all()
    print("=================",employes)
    return render(request, "display.html", {"record": employes})