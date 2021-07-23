from django.http.response import HttpResponse
from crudapp.forms import EmployeeForms
from django.shortcuts import redirect, render
from .models import Employee
from .forms import EmployeeForms


def homeView(request):
    return render(request, 'home.html')


def createView(request):
    if request.method == "POST":
        form = EmployeeForms(request.POST)
        if form.is_valid():
            try:
                form.save()
                # return HttpResponse("Successfully Submitted")
                return redirect('/retrive')
            except:
                print("not saved")
                
    else:
        form = EmployeeForms()
        return render(request, 'create.html', {'form': form})


def retrieveView(request):
    employee = Employee.objects.all()
    return render(request, 'retrieve.html', {'employee': employee})




def deleteView(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/retrive")  

def editView(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  




















def updateView(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForms(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/retrive")  
    return render(request, 'edit.html', {'employee': employee})  



