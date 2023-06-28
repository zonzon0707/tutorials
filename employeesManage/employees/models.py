from django.db import models

# Create your models here.


class Employee(models.Model):
    employeeId = models.IntegerField()
    employeeName = models.CharField(max_length = 255)

