from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View

from django.views.decorators.csrf import csrf_exempt

from .models import Persons

# Create your views here.

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
        import pdb
        pdb.set_trace()
        data = request.POST['data']
    
def yash(request):
    a=("aBc. DEF".capitalize())
    return HttpResponse(a)