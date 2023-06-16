from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmployeeApp.models import Departments , Employee
from EmployeeApp.serializers import DepartmentSerializer , EmployeeSerializer
# Create your views here.


@csrf_exempt
def departmentApi (request , id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer  = DepartmentSerializer(departments , many = True)
        return JsonResponse(departments_serializer.data  , safe= False)
    

    elif request.method == 'POST':
        departments_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data = departments_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Records Added Successfully" ,safe=False)
        return JsonResponse("Failed to add" , safe=False)
    

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(department , data = department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully" , safe=False)
        return JsonResponse("Failed to update")
    
    elif request.method == 'DELETE':
        departmentt= Departments.objects.get(DepartmentId = id)
        departmentt.delete()
        return JsonResponse("Deleted Successfully" , safe=False)


@csrf_exempt
def employeeApi (request , id=0):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employees_serializer  = EmployeeSerializer( employees, many = True)
        return JsonResponse(employees_serializer.data  , safe= False)
    

    elif request.method == 'POST':
        employees_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data = employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Records Added Successfully" ,safe=False)
        return JsonResponse("Failed to add" , safe=False)
    

    elif request.method == 'PUT':
        employees_data = JSONParser().parse(request)
        employee = Employee.objects.get(EmployeeId = employees_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee , data = employees_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully" , safe=False)
        return JsonResponse("Failed to update")
    
    elif request.method == 'DELETE':
        employee=Employee.objects.get(EmployeeId = id)
        employee.delete()
        return JsonResponse("Deleted Successfully" , safe=False)




