from django.shortcuts import render , redirect
from newapp.models import Employee

# Create your views here.

def index(request) :
    employee = Employee.objects.all()
    return render (request , 'newapp/index.html', {'employee' : employee})

def details(request, id) :
    employee = Employee.objects.get(id=id)
    return render (request,'newapp/details.html',{'employee' : employee})

def create(request) :
    if request.POST :
        new_employee = Employee(name = request.POST['name'],age = request.POST['age'],department = request.POST['department'],salary = request.POST['salary'])
        new_employee.save()
        return redirect('/newapp/')
    return render (request, 'newapp/create.html')