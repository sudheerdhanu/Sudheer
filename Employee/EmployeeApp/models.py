from django.db import models
class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.IntegerField()
    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.eid

class AcceptedList(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    class Meta:
        db_table = "AcceptedList"

    def __str__(self):
        return self.ename

class AdminRegister(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    conform_password=models.CharField(max_length=20)
    Email=models.EmailField(max_length=20)
    mobile=models.IntegerField()

    def __str__(self):
        return self.fname


