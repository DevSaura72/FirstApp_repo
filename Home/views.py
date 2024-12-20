from operator import __le__
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from datetime import datetime
from .models import UDC, Employee
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings

# Create your views here.

def index(request):
    context = {
        "var" : "This is sent by SAURABH SHETH"
    }
    return render(request, 'index.html')

#EMPLOYEE RELATED FUNCTIONS    
def emplMaster(request):
    department = UDC.objects.filter(IsHeader = False, IsDeleted = False, ParentId= 1)
    workLocations = UDC.objects.filter(IsHeader = False, IsDeleted = False, ParentId= 4)
    employeeType = UDC.objects.filter(IsHeader = False, IsDeleted = False, ParentId= 7)
    return render(request, 'EmpMaster.html', {'department': department, 'workLocations': workLocations, 'employeeType': employeeType, 'edit':False})

def GetemployeeData(request):
    emp = Employee.objects.filter(IsDeleted = False)

# Get the search filters from the request (using request.GET for GET requests)
    contact_no = request.GET.get('contactNo', '')
    dep_id = request.GET.get('depId', '')
    email_id = request.GET.get('emailId', '')
    emp_type_id = request.GET.get('empTypeId', '')
    f_name = request.GET.get('fName', '')
    is_active = request.GET.get('isActive', '')  # "on" or empty string
    l_name = request.GET.get('lName', '')
    work_location_id = request.GET.get('workLocationId', '')
    add = request.GET.get('add','')
    

    # Apply filters based on the parameters passed in the request
    if contact_no:
        emp = emp.filter(ContactNo__icontains=contact_no)  
    if dep_id:
        emp = emp.filter(DepartmentId__id=dep_id)
    if email_id:
        emp = emp.filter(EmailId__icontains=email_id)
    if emp_type_id:
        emp = emp.filter(EmploymentTypeID__id=emp_type_id)
    if f_name:
        emp = emp.filter(FirstName__icontains=f_name)
    if l_name:
        emp = emp.filter(LastName__icontains=l_name)
    if work_location_id:
        emp = emp.filter(WorkLocationID__id=work_location_id)
    if add:
        emp = emp.filter(Address__icontains=add)
    
    
    # if is_active == 'true':  
    #     emp = emp.filter(IsDeleted=False)
    # elif is_active == 'false':  
    #     emp = emp.filter(IsDeleted=True)


    _list = []
    for record in emp:
        
        Dept = UDC.objects.filter(id=record.DepartmentId.id if record.DepartmentId else None, IsDeleted=False).first()
        dept_name = Dept.val1 if Dept else None
        
        EmpType = UDC.objects.filter(id=record.EmploymentTypeID.id if record.EmploymentTypeID else None, IsDeleted=False).first()
        empType_name = EmpType.val1 if EmpType else None
        
        WorkLocation = UDC.objects.filter(id=record.WorkLocationID.id if record.WorkLocationID else None, IsDeleted=False).first()
        workLocation_name = WorkLocation.val1 if WorkLocation else None
        # Append the required data, including the parent name
        _list.append({
            'id': record.id,
            'FirstName': record.FirstName,
            'LastName': record.LastName,
            'DOB': record.DOB.strftime('%Y-%m-%d'),
            'EmailId': record.EmailId,
            'ContactNo': record.ContactNo,
            'Address': record.Address.replace("|",", "),
            'DepartmentId': dept_name,
            'EmploymentTypeID': empType_name,
            'WorkLocationID': workLocation_name,
            'IsDeleted': record.IsDeleted
        })
    total_entries = emp.count()
    return JsonResponse({
        'data': _list,
        #'draw' : command.draw,
        'recordsFiltered' : total_entries,
        'recordsTotal' : total_entries
    })

def AddEmployee(request):
    try:
        department = UDC.objects.filter(IsHeader = False, IsDeleted = False, ParentId= 1)
        workLocations = UDC.objects.filter(IsHeader = False, IsDeleted = False, ParentId= 4)
        employeeType = UDC.objects.filter(IsHeader = False, IsDeleted = False, ParentId= 7)
        if request.method == "POST":
            fName=request.POST.get("fName")
            lName=request.POST.get("lName")
            dOB= request.POST.get("dob")
            eId=request.POST.get("emailId")
            cNo=request.POST.get("contactNo")
            add=request.POST.get("addLine1") + "|" + request.POST.get("addLine2") + "|" + request.POST.get("city") + "|" + request.POST.get("state") + "|" + request.POST.get("pinCode")
            depId=request.POST.get("depId")
            empTypeID = request.POST.get("employeeTypeId")
            workLocationID = request.POST.get("workLocationId")

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
            return render(request, 'EmployeeAddUpdate.html', {'department': department, 'workLocations': workLocations, 'employeeType': employeeType, 'edit':False})
        else:
             return render(request, 'EmployeeAddUpdate.html', {'department': department, 'workLocations': workLocations, 'employeeType': employeeType, 'edit':False})
    except Exception as e:
            return HttpResponse(f"Error occurred now: {e}")
    
def deleteEmployee(request, id):
    try:
        emp = Employee.objects.get(id=id)
        emp.IsDeleted = True
        emp.save()
        messages.success(request, "Employee deleted successfuly .")
    except Employee.DoesNotExist:
        #messages.error(request, "Employee not found.")
        return render(request, 'EmpMaster.html', {'error': 'Employee not found.'})
    return redirect('emplMaster')

def editEmployee(request, id):
# Fetch the employee instance or return 404 if not found
    employee = get_object_or_404(Employee, id=id)
    employee.DOB = employee.DOB.strftime('%Y-%m-%d') 
    # Fetch dropdown data for departments, work locations, and employee types
    department = UDC.objects.filter(IsHeader=False, IsDeleted=False, ParentId= 1)
    workLocations = UDC.objects.filter(IsHeader=False, IsDeleted=False, ParentId= 4)
    employeeType = UDC.objects.filter(IsHeader=False, IsDeleted=False, ParentId= 4)
    address_parts = employee.Address.split('|') if employee.Address else ['', '', '', '','']


    if request.method == "POST":
        # Get data from the form
        fName = request.POST.get("fName")
        lName = request.POST.get("lName")
        dOB = request.POST.get("dob") 
        eId = request.POST.get("emailId")
        cNo = request.POST.get("contactNo")
        add = request.POST.get("addLine1") + "|" + request.POST.get("addLine2") + "|" + request.POST.get("city") + "|" + request.POST.get("state") + "|" + request.POST.get("pinCode")
        depId = request.POST.get("depId")
        empTypeID = request.POST.get("employeeTypeId")
        workLocationID = request.POST.get("workLocationId")

        # Update employee fields
        employee.id = id
        employee.FirstName = fName
        employee.LastName = lName
        employee.DOB = dOB
        employee.EmailId = eId
        employee.ContactNo = cNo
        employee.Address = add
        employee.DepartmentId = UDC.objects.get(id=depId) if depId and depId != '0' else None
        employee.EmploymentTypeID = UDC.objects.get(id=empTypeID) if empTypeID and empTypeID != '0' else None
        employee.WorkLocationID = UDC.objects.get(id=workLocationID) if workLocationID and workLocationID != '0' else None
        employee.UpdatedOn = datetime.now()  # Set updated timestamp

        # Save the updated employee record
        employee.save()
        messages.success(request, "Employee details updated successfully.")
        return redirect('emplMaster')  # Redirect to the employee list or another appropriate page

    # Prepopulate the form with existing employee data
    context = {
        'employee': employee,
        'department': department,
        'workLocations': workLocations,
        'employeeType': employeeType,
        'address_parts': address_parts,
    }
    return render(request, 'EmployeeUpdate.html', context)


#UDC RELATED FUNCTIONS
def UDCAddHeader(request):
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
             return render(request, 'UDCAdd.html', {'isHeader': True})
        else:
             return render(request, 'UDCAdd.html', {'isHeader': True})
    except Exception as e:
            return HttpResponse(f"Error occurred now: {e}")

def UDCAddData(request):
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
             return render(request, 'UDCAdd.html', {'isHeader': False, 'parents': parents, 'relations' : relations})
        else:
             return render(request, 'UDCAdd.html', {'isHeader': False, 'parents': parents, 'relations' : relations})
    except Exception as e:
            return HttpResponse(f"Error occurred now: {e}")


def editUDCHeader(request, id):
     try:
          header = UDC.objects.get(id = id)

          if request.method == "POSt":
               header.id = request.get('')
               return redirect('UDCMaster')
     except UDC.DoesNotExist:
          messages.error(request, "Not found.")
     return render(request, 'UDCUpdate.html', {'isHeader' : True, 'udc':header})

def deleteUDCHeader(request, id):
     try:
          header = UDC.objects.get(id = id)
          header.IsDeleted = True
          header.save()
     except UDC.DoesNotExist:
          messages.error(request, "Not found.")
     return redirect('UDCMaster')

def editUDCData(request, id):
     try:
        parents = UDC.objects.filter(IsHeader = True, IsDeleted = False)
        relations = UDC.objects.filter(IsHeader = False, IsDeleted = False)
        header = UDC.objects.get(id = id)

        if request.method == "POSt":
               header.id = request.get('')
               return redirect('UDCMaster')
     except UDC.DoesNotExist:
          messages.error(request, "Not found.")
     return render(request, 'UDCUpdate.html', {'isHeader' : False, 'udc':header, 'parents': parents, 'relations' : relations})
     
def deleteUDCData(request, id):
     try:
          data = UDC.objects.get(id = id)
          data.IsDeleted = True
          data.save()
     except data.DoesNotExist:
          messages.error(request, "Not found.")
     return redirect('UDCMaster')




def contact(request):
    return render(request, 'contact.html')

def UDCMaster(request):
    udc = UDC.objects.filter(IsHeader = False, IsDeleted = False)
    headers = UDC.objects.filter(IsHeader = True, IsDeleted = False)
    return render(request, 'UDCMaster.html', {'udcs': udc, 'headers' : headers})

def GetUDCHeaders(request):
    #udc = UDC.objects.filter(IsHeader = False, IsDeleted = False)
    headers = UDC.objects.filter(IsHeader = True, IsDeleted = False)
    headers_list = list(headers.values('id', 'Header', 'IsHeader', 'description', 'IsDeleted'))
    a = len(headers_list)
    return JsonResponse({'data': headers_list,
        'recordsFiltered' : a,
        'recordsTotal' : a })

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
             'id': record.id,
            'val1': record.val1,
            'val2': record.val2,
            'description': record.description,
            'ParentId': parent_name,
            'RelationId': relation_name,
            'IsDeleted': record.IsDeleted,
        })

    a = len(_list)
    return JsonResponse({'data': _list,
        'recordsFiltered' : a,
        'recordsTotal' : a })

     

def test(request):
    return render(request, 'test.html')