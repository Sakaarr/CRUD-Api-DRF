from django.urls import path
from . import views

urlpatterns = [
    path('departments' , views.departmentApi),
    path('departments/<int:id>', views.departmentApi),

    path('employee' , views.employeeApi),
    path('employee/<int:id>', views.employeeApi),
]

