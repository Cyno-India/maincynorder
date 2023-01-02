from django.db import models
from user.models import *

# Create your models here.
class ItemCard(models.Model): 
    No = models.CharField(max_length=20,default="")
    Description = models.CharField(max_length=50,default="")
    Box_No = models.CharField(max_length=25,default="")
    AssemblyBOM = models.CharField(max_length=25,default="")
    Sales_Unit_of_Measure = models.CharField(max_length=25,default="")
    Net_Weight =  models.CharField(max_length=25,default="")

class BomAssemblyTable(models.Model):
    Parent_Item_No = models.CharField(max_length=20,default="")   
    No = models.CharField(max_length=50,default="")
    Description= models.CharField(max_length=25,default="")
    AssemblyBOM = models.CharField(max_length=25,default="")
    Quantity_per = models.CharField(max_length=25,default="")
    unit_measure_code = models.CharField(max_length=25,default="")


class Weight(models.Model):
    Document_No = models.CharField(max_length=20,default="")   
    Line_No = models.CharField(max_length=50,default="")
    Courier_Channel= models.CharField(max_length=25,default="")
    Country = models.CharField(max_length=25,default="")
    From_Weight = models.CharField(max_length=25,default="")
    To_Weight = models.CharField(max_length=25,default="")
    Amount = models.CharField(max_length=25,default="")
    C_num = models.CharField(max_length=25,default="")

