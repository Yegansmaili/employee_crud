from django import forms
from .models import *


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'national_code', 'phone_number', 'position', 'salary', 'is_employed']


class UploadFileForm(forms.Form):
    file = forms.FileField()
