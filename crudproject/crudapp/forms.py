from django import forms
from django.db.models import fields
from django.db.models.base import Model

from crudapp.models import Employee



class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
