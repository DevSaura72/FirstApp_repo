from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import UDC, Employee
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

def index(request):
    context = {
        "var" : "This is sent by SAURABH SHETH"
    }
    return render(request, 'index.html')

def AddEmployee(request):
    try:
        department = UDC.objects.filter(IsHeader = False, IsDeleted = False, ParentId = 4)
        workLocations = UDC.objects.filter(IsHeader = False, IsDeleted = False, ParentId = 7)
        employeeType = UDC.objects.filter(IsHeader = False, IsDeleted = False, ParentId = 10)
        if request.method == "POST":
            fName=request.POST.get("fName")
            lName=request.POST.get("lName")
            dOB= "1998-08-24"               #request.POST.get("dob")
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

def GetUDCHeaders(request):
    #udc = UDC.objects.filter(IsHeader = False, IsDeleted = False)
    headers = UDC.objects.filter(IsHeader = True, IsDeleted = False)
    headers_list = list(headers.values('id', 'Header', 'IsHeader', 'description', 'IsDeleted'))
    return JsonResponse({'data': headers_list})

def GetUDCData(request):

    udc_records = UDC.objects.filter(IsHeader=False, IsDeleted=False)
    
    _list = []
    for record in udc_records:
        # Attempt to find the parent UDC record based on ParentId
        parent_record = UDC.objects.filter(id = record.ParentId, IsHeader=True).first()
        parent_name = parent_record.Header if parent_record else None
        Relation_record = UDC.objects.filter(id = record.RelationId, IsHeader=True).first()
        relation_name = Relation_record.val1 if Relation_record else None
        
        # Append the required data, including the parent name
        _list.append({
            'val1': record.val1,
            'val2': record.val2,
            'description': record.description,
            'ParentId': parent_name,
            'RelationId': relation_name,
            'IsDeleted': record.IsDeleted,
        })

    return JsonResponse({'data': _list})

def GetemployeeData(request):
    #udc = UDC.objects.filter(IsHeader = False, IsDeleted = False)
    emp = Employee.objects.filter(IsDeleted = False)
    emp_list = list(emp.values('id', 'FirstName', 'LastName', 'DOB', 'EmailId', 'ContactNo', 'Address', 'DepartmentId', 'EmploymentTypeID', 'WorkLocationID', 'IsDeleted'))
    return JsonResponse({'data': emp_list})

def deleteEmployee(request, id):
     return render(request, 'test.html')

def editEmployee(request, id):
     # Fetch the employee instance or return 404 if not found
    employee = Employee.objects.filter(Employee, id=id)
    
    # Fetch dropdown data for departments, work locations, and employee types
    department = UDC.objects.filter(IsHeader=False, IsDeleted=False, ParentId=4)
    workLocations = UDC.objects.filter(IsHeader=False, IsDeleted=False, ParentId=7)
    employeeType = UDC.objects.filter(IsHeader=False, IsDeleted=False, ParentId=10)

    if request.method == "POST":
        # Get data from the form
        fName = request.POST.get("fName")
        lName = request.POST.get("lName")
        dOB = request.POST.get("dob")  # Make sure the input for DOB is a valid date format
        eId = request.POST.get("emailId")
        cNo = request.POST.get("contactNo")
        add = request.POST.get("addLine1") + "|" + request.POST.get("addLine2") + "|" + request.POST.get("state") + "|" + request.POST.get("pinCode")
        depId = request.POST.get("depId")
        empTypeID = request.POST.get("employeeTypeId")
        workLocationID = request.POST.get("workLocationId")

        # Update employee fields
        employee.FirstName = fName
        employee.LastName = lName
        employee.DOB = dOB
        employee.EmailId = eId
        employee.ContactNo = cNo
        employee.Address = add
        employee.DepartmentId = UDC.objects.get(id=depId) if depId else None
        employee.EmploymentTypeID = UDC.objects.get(id=empTypeID) if empTypeID else None
        employee.WorkLocationID = UDC.objects.get(id=workLocationID) if workLocationID else None
        employee.UpdatedOn = datetime.now()  # Set updated timestamp

        # Save the updated employee record
        employee.save()
        messages.success(request, "Employee details updated successfully.")
        return redirect('employee_list')  # Redirect to the employee list or wherever needed

    else:
        # Prepopulate the form with existing employee data
        context = {
            'employee': employee,
            'department': department,
            'workLocations': workLocations,
            'employeeType': employeeType,
        }
        return render(request, 'EmployeeAddUpdate.html', context)

def test(request):
    return render(request, 'test.html')