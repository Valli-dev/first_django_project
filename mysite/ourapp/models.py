from django.db import models
from datetime import datetime

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length= 400)
    
    def __str__(self):
        return self.name


class Faculty(models.Model):
    name=models.CharField(max_length=400)

    def __str__(self):
        return self.name



class Certificate_type(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Grade(models.Model):
    type=models.CharField(max_length=50)

    def __str__(self):
        return self.type



class Department(models.Model):
    name=models.CharField(max_length=400)
    Faculty=models.ForeignKey(Faculty, on_delete= models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    fullname= models.CharField(max_length = 50)
    year_of_graduation=models.DateField(default=datetime.today)
    Department = models.ForeignKey(Department, on_delete = models.PROTECT)
    Grade=models.ForeignKey(Grade, on_delete=models.PROTECT)
    School = models.ForeignKey(School, on_delete = models.CASCADE)
    Certificate_type=models.ForeignKey(Certificate_type,on_delete=models.PROTECT)
   
    def __str__(self):
        return self.fullname
