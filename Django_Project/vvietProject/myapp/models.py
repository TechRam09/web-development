from django.db import models

# Create your models here.
class College(models.Model):
    collegeName = models.CharField(max_length=25)    
    location = models.CharField()
    totalstudent = models.IntegerField()
    pincode = models.IntegerField()
    def __str__(self):
        return self.collegeName +"("+ self.location + ")"