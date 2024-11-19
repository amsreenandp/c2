from django.db import models

# Create your models here.
class item(models.Model): 
   itemdis = models.CharField(max_length = 50)
   itemname = models.CharField(max_length = 50)
   itemid = models.IntegerField()
   price = models.IntegerField()
