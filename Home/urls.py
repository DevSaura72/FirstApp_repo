from django.contrib import admin
from django.urls import path
from Home import views


urlpatterns = [
    path('', views.index, name='home'),

    path('addEmployee', views.AddEmployee, name='addEmployee'),
    path('GetemployeeData', views.GetemployeeData, name='GetemployeeData'),
    path('editEmployee/<int:id>/', views.editEmployee, name='editEmployee'),
    path('deleteEmployee/<int:id>/', views.deleteEmployee, name='deleteEmployee'),

    path('UDCMaster', views.UDCMaster, name='UDCMaster'),
    path('GetUDCHeaders', views.GetUDCHeaders, name='GetUDCHeaders'),
    path('GetUDCData', views.GetUDCData, name='GetUDCData'),
    path('UDCAddHeader', views.UDCAddHeader, name='UDCAddHeader'),
    path('UDCAddData', views.UDCAddData, name='UDCAddData'),

    #path('empMaster', views.empMaster, name='empMaster'),
    path('contact', views.contact, name='contact'),
    path('emplMaster', views.emplMaster, name='emplMaster'),
    path('test', views.test, name='test'),
]