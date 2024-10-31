from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import UDC, Employee
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        "var" : "This is sent by SAURABH SHETH"
    }
    return render(request, 'index.html')

def AddEmployee(request):
    try:
        department = UDC.objects.filter(IsHeader = False, IsDeleted = False, ParentId = 1)
        workLocations = UDC.objects.filter(IsHeader = False, IsDeleted = False, ParentId = 4)
        employeeType = UDC.objects.filter(IsHeader = False, IsDeleted = False, ParentId = 7)
        if request.method == "POST":
            fName=request.POST.get("fName")
            lName=request.POST.get("lName")
            dOB=request.POST.get("dob")
            eId=request.POST.get("emailId")
            cNo=request.POST.get("contactNo")
            add=request.POST.get("addLine1") + "|" + request.POST.get("addLine2") + "|" + request.POST.get("state") + "|" + request.POST.get("pinCode")
            depId=request.POST.get("depId")
            empTypeID=request.POST.get("workLocationId")
            workLocationID = request.POST.get("employeeTypeId")

            #  if request.POST.get("isActive") == "true":
            #       isActive = True
            #  else:
            #       isActive = False     

            emp = Employee( 
                FirstName=fName,
                LastName=lName,
                DOB=dOB,
                EmailId=eId,
                ContactNo=cNo,
                Address=add,
                DepartmentId= UDC.objects.get(id=depId) if depId else None,
                EmploymentTypeID=UDC.objects.get(id=empTypeID) if depId else None,
                WorkLocationID = UDC.objects.get(id=workLocationID) if depId else None,
                CreatedOn = datetime.now(),
                CreatedBy = 0
                )
            
            emp.save()
            messages.success(request, "Profile details updated.")
            return render(request, 'EmployeeAddUpdate.html', {'department': department, 'workLocations': workLocations, 'employeeType': employeeType})
        else:
             return render(request, 'EmployeeAddUpdate.html', {'department': department, 'workLocations': workLocations, 'employeeType': employeeType})
    except Exception as e:
            return HttpResponse(f"Error occurred now: {e}")

def empMaster(request):
    return render(request, 'EmployeeMasterIndex.html')
    
def UDCAddUpdate(request):
    try:
        parents = UDC.objects.filter(IsHeader = True, IsDeleted = False)
        relations = UDC.objects.filter(IsHeader = False, IsDeleted = False)
        if request.method == "POST":
             hea = request.POST.get("header")
             v1 = request.POST.get("val1")
             v2 = request.POST.get("val2")
             parId = request.POST.get("parentId")
             relId = request.POST.get("relationId")
             desc = request.POST.get("Description")
             if request.POST.get("isHeader") == "true":
                  isHead = True
             else:
                  isHead = False     

             udc = UDC(
                Header=hea,
                val1=v1,
                val2=v2,
                description=desc,
                ParentId=parId,
                RelationId=relId,
                CreatedBy=0,
                CreatedOn=datetime.now(),
                UpdatedBy=0,
                IsHeader = isHead
                )
             udc.save()
             messages.success(request, "Profile details updated.")
             return render(request, 'UDCAddUpdate.html', {'parents': parents, 'relations': relations})
        else:
             return render(request, 'UDCAddUpdate.html', {'parents': parents, 'relations': relations})
    except Exception as e:
            return HttpResponse(f"Error occurred now: {e}")

def contact(request):
    return render(request, 'contact.html')

def emplMaster(request):
    employees = Employee.objects.all()
    return render(request, 'EmpMaster.html', {'employees': employees})

def UDCMaster(request):
    udc = UDC.objects.filter(IsHeader = False, IsDeleted = False)
    headers = UDC.objects.filter(IsHeader = True, IsDeleted = False)
    return render(request, 'UDCMaster.html', {'udcs': udc, 'headers' : headers})
