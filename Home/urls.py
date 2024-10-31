from django.contrib import admin
from django.urls import path
from Home import views


urlpatterns = [
    path('', views.index, name='home'),
    path('addEmployee', views.AddEmployee, name='addEmployee'),
    path('UDCAddUpdate', views.UDCAddUpdate, name='UDCAddUpdate'),
    path('empMaster', views.empMaster, name='empMaster'),
    path('contact', views.contact, name='contact'),
    path('emplMaster', views.emplMaster, name='emplMaster'),
    path('UDCMaster', views.UDCMaster, name='UDCMaster'),
]