from django import forms
from EmployeeApp.models import Employee, AdminRegister


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class AdminRegisterForm(forms.ModelForm):
    class Meta:
        model=AdminRegister
        fields="__all__"


class LoginForm(forms.Form):
    username=forms.CharField(
        label="User Name",
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    password = forms.CharField(
        label="User Name",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )