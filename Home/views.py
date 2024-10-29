from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import UDC

# Create your views here.

def index(request):
    context = {
        "var" : "This is sent by SAURABH SHETH"
    }
    return render(request, 'index.html')

def AddEmployee(request):
    department = UDC.objects.filter(IsHeader = False, IsDeleted = False)
    #relations = UDC.objects.all(IsHeader = False, IsDeleted = False, ParentId = 4)
    return render(request, 'EmployeeAddUpdate.html', {'department': department})

# def AddEmployee(request):
#     Department = UDC.objects.filter(IsHeader = False, IsDeleted = False, ParentId = 1)
#     #relations = UDC.objects.all(IsHeader = False, IsDeleted = False, ParentId = 4)
#     return render(request, 'EmployeeAddUpdate.html', {'parents': Department})

def UDCAddUpdate(request):
         parents = UDC.objects.filter(IsHeader = True, IsDeleted = False)
         relations = UDC.objects.filter(IsHeader = True, IsDeleted = False)
         return render(request, 'UDCAddUpdate.html', {'parents': parents, 'relations': relations})

def AddUDC(request):
        try:
            # hea = request.POST.get("header")
            # v1 = request.POST.get("val1")
            # v2 = request.POST.get("val2")
            # parId = request.POST.get("parentId")
            # relId = request.POST.get("relationId")
            # desc = request.POST.get("Description")

            # udc = UDC(
            #     Header=hea,
            #     val1=v1,
            #     val2=v2,
            #     description=desc,
            #     ParentId=parId,
            #     RelationId=relId,
            #     CreatedBy=0,
            #     CreatedOn=datetime.now(),
            #     UpdatedBy=0
            # )
            # udc.save()
         parents = UDC.objects.filter(IsHeader = True, IsDeleted = False)
         relations = UDC.objects.all(IsHeader = True, IsDeleted = False)
         return render(request, 'UDCAddUpdate.html', {'parents': parents, 'relations': relations})
        except Exception as e:
            return HttpResponse(f"Error occurred: {e}")

def contact(request):
    return render(request, 'contact.html')
