from django.db import models

class UDC(models.Model):
    #ID = models.AutoField(primary_key=True)
    Header = models.CharField(max_length=50, null=True, blank=True)
    IsHeader = models.BooleanField(default=True)
    val1 = models.CharField(max_length=50, null=True, blank=True)
    val2 = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=800)
    ParentId = models.IntegerField(null=True, blank=True, default=0)
    RelationId = models.IntegerField(null=True, blank=True, default=0)
    CreatedBy = models.IntegerField()
    CreatedOn = models.DateField()

    UpdatedBy = models.IntegerField(null=True, blank=True)
    UpdatedOn = models.DateField(null=True, blank=True)
    DeletedBy = models.IntegerField(null=True, blank=True)
    DeletedOn = models.DateField(null=True, blank=True)

    IsDeleted = models.BooleanField(default=False)



class Employee(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    DOB = models.DateField()
    EmailId = models.CharField(max_length=120) 
    ContactNo = models.CharField(max_length=13) 
    Address = models.CharField(max_length=800)

    DepartmentId = models.ForeignKey(UDC, on_delete=models.CASCADE, related_name='employees_in_department')
    EmploymentTypeID = models.ForeignKey(UDC, on_delete=models.CASCADE, related_name='employees_with_employment_type')
    WorkLocationID = models.ForeignKey(UDC, on_delete=models.CASCADE, related_name='employees_in_work_location')

    CreatedBy = models.IntegerField()
    CreatedOn = models.DateField()

    UpdatedBy = models.IntegerField(null=True, blank=True)
    UpdatedOn = models.DateField(null=True, blank=True)
    DeletedBy = models.IntegerField(null=True, blank=True)
    DeletedOn = models.DateField(null=True, blank=True)

    IsDeleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"
