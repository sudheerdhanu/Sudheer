from django.shortcuts import render, redirect
from django.http import HttpResponse
from EmployeeApp.forms import AdminRegisterForm, LoginForm, EmployeeForm
from  EmployeeApp.models import Employee,AdminRegister,AcceptedList

from django.contrib import auth


def home(request):
    return render(request,'home.html')



def register(request):
    if request.method == 'POST':
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AdminRegisterForm()
    return render(request, 'login/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':

        lform=LoginForm(request.POST)
        if lform.is_valid():
            username=request.POST.get('username','')
            password=request.POST.get('password','')
            user=AdminRegister.objects.filter(username=username)
            password=AdminRegister.objects.filter(password=password)

            print(user,password)

            if user and password:
                return redirect('/show')
            else:
                return HttpResponse("<h1>Invalid Credentials</h1>")
    else:
        form=LoginForm()
        return render(request, 'login/login.html', {'form':form})


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request,'remainder.html',{'data':"Application Submitted Sucessfully"})
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})


def show(request):
    employees = Employee.objects.all()
    return render(request,"show.html",{'employees':employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)

    AcceptedList.objects.create(eid=employee.eid,
                                ename=employee.ename,
                                eemail=employee.eemail,
                                econtact=employee.econtact)

    employee.delete()
    return redirect("/show")


def accept(request):
    data=AcceptedList.objects.all()
    return render(request,'accept.html',{"data":data})



def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")