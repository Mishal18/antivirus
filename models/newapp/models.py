from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    department = models.CharField(max_length=30)
    salary = models.DecimalField(decimal_places=3 , max_digits=10)

    def __str__(self) :
        return self.name