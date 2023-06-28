# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Employee


def employees(request):
    # return HttpResponse("HELLO WORLD!!!")

    # template = loader.get_template('myfirst.html')
    # return HttpResponse(template.render())
    if 'searchButton' in request.POST and request.POST.get('searchId'):
        myEmployees = Employee.objects.filter(employeeId = int(request.POST.get('searchId')))
    else:
        myEmployees = Employee.objects.all().values()

    context = {
        'myEmployees' : myEmployees,
    }
    template = loader.get_template('all_employees.html')
    return HttpResponse(template.render(context, request))

def details(request, id):
    myEmployees = Employee.objects.get(id = id)
    template = loader.get_template('details.html')
    context = {
        'myEmployees' : myEmployees,
    }
    return HttpResponse(template.render(context, request))