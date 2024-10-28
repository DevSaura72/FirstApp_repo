from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import UDC

# Create your views here.

def index(request):
    context = {
        "var" : "This is sent by SAURABH SHETH"
    }
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def UDCAddUpdate(request):
    if request.method == "POST":
        hea = request.POST.get("header")
        v1 = request.POST.get("val1")
        v2 = request.POST.get("val2")
        parId = request.POST.get("parentId")
        relId = request.POST.get("relationId")
        desc = request.POST.get("Description")
        # udc = UDC(Header = hea, val1 = v1, val2 = v2, description = desc, ParentId = parId, RelationId = relId, 
        #           CreatedBy = 0, CreatedOn = datetime.now(), UpdatedBy = 0, UpdatedOn = datetime.now(), DeletedBy = 0, DeletedOn= datetime.now(), IsDeleted = False)
        udc = UDC(Header = hea, val1 = v1, val2 = v2, description = desc, ParentId = parId, RelationId = relId, 
                  CreatedBy = 0, CreatedOn = datetime.now(), UpdatedBy = 0)
        udc.save()

    return render(request, 'UDCAddUpdate.html')

def contact(request):
    return render(request, 'contact.html')
