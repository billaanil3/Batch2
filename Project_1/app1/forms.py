from django import forms
from .models import NagStudent

class NagStudentForm(forms.Form):
    sid = forms.IntegerField(label="Enter SID")
    lastName = forms.CharField(label="Enter LastName")
    firstName = forms.CharField(label="Enter FirstName")
    subjectName = forms.CharField(label="Enter SubjectName")


class NagStudentModelForm(forms.ModelForm):
    class Meta:
        model = NagStudent
        fields = ['st_id', "last_name", "firstname", "sc_name"]

