from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=30)
    eid=models.IntegerField(default=0)

    def __str__(self):
        return self.firstname