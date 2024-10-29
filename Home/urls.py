from django.contrib import admin
from django.urls import path
from Home import views


urlpatterns = [
    path('', views.index, name='home'),
    path('EmployeeAddUpdate', views.AddEmployee, name='EmployeeAddUpdate'),
    path('addEmployee', views.AddEmployee, name='addEmployee'),
    path('UDCAddUpdate', views.UDCAddUpdate, name='UDCAddUpdate'),
    # path('AddUDC', views.AddUDC, name='AddUDC'),
    path('contact', views.contact, name='contact'),
]