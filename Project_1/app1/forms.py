from django import forms
from .models import NagStudent
from .models import Employee

class NagStudentForm(forms.Form):
    sid = forms.IntegerField(label="Enter SID")
    lastName = forms.CharField(label="Enter LastName")
    firstName = forms.CharField(label="Enter FirstName")
    subjectName = forms.CharField(label="Enter SubjectName")


class NagStudentModelForm(forms.ModelForm):
    class Meta:
        model = NagStudent
        fields = ['st_id', "last_name", "firstname", "sc_name"]

class EmployeeForm(forms.Form):
    eId = forms.IntegerField(label="Enter EID")
    eName = forms.CharField(label="Enter EName")
    eInitial = forms.CharField(label="Enter EInitial")
    cName = forms.CharField(label="Enter cNamae ")
    area = forms.CharField(label="Enter Area")


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['EmpId', "Name", "Initial", "CompanyName","Area"]

