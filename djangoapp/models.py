from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# class Operating_system(models.Model):
#     operating_system = models.CharField(max_length=30, blank=True)
#
#     def __str__(self):
#         return self.operating_system

class Computer(models.Model):
    computer_name = models.CharField(max_length=100,blank=True)
    IP_address = models.CharField(max_length=100)
    MAC_address = models.CharField(max_length=100,blank=True)
    # operating_system = models.ForeignKey(Operating_system,on_delete=models.CASCADE, blank=True, null=True)
    users_name = models.CharField(max_length=100,blank=True)
    location = models.CharField(max_length=100,blank=True)
    price = models.CharField(max_length=100,blank=True,null=True)
    purchase_date = models.DateTimeField('purchase Date(dd/mm/2020)',auto_now_add=False,auto_now=False,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False,blank=True)
    export_to_CSV = models.BooleanField(default=False)

    def __unicode__(self):
        return self.computer_name


class ComputerHistory(models.Model):
    computer_name = models.CharField(max_length=100, blank=True, null=True)
    IP_address = models.CharField(max_length=100, blank=True, null=True)
    MAC_address = models.CharField(max_length=30, blank=True, null=True)
    users_name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    purchase_date = models.DateField("Purchase Date(mm/dd/2019)", auto_now_add=False, auto_now=False, blank=True,
                                     null=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True, null=True)

