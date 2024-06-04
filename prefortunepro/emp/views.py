from django.shortcuts import render
from .forms import emp_reg

# Create your views here.
def index(request):
    if request.method=='POST':
        employee=emp_reg(request.POST)
        if employee.is_valid():
            employee.save()
            print("sucess!!!")
        else:
            print(employee.errors)
    return render(request,'index.html')