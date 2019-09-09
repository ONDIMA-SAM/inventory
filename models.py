from django.db import models

# Create your models here.
class Equipment(models.Model):
    type = models.CharField(max_length=8)
    mac_address = models.CharField(max_length=20)
    serial_number= models.CharField(max_length=20)
    vendor = models.CharField(max_length=15)
    status = models.CharField(max_length=15)
    assigned_to = models.CharField(max_length=15, default='Not assigned')
    department = models.CharField(max_length=15, default='store')
    class Meta:
        ordering = ('id',)
