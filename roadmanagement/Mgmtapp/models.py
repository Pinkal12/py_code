from django.db import models

# Create your models here.
class SDO(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    number_MC = models.CharField(max_length=20)
    # type = models.CharField(max_length=10)


    def __str__(self):
        return self.name
  
sdo = SDO.objects.create(name="xyz",email="xyz@gmail.com",password="12345",phone="64873648434",number_MC="mgrateh")
sdo.save()