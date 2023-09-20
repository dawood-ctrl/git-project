from django.db import models
# Create your models here.

class students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Email = models.EmailField()
    dob = models.DateField()
    roll_no = models.IntegerField()

class course(models.Model):
    Course_name = models.CharField(max_length=50)
    credits_hours = models.IntegerField()
    subjects = models.CharField(max_length=50)
    Students = models.ManyToManyField(students)