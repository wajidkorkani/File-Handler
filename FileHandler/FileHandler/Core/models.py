from django.db import models

# Create your models here.

class File(models.Model):
    document = models.FileField(upload_to='uploads/', null=True)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True) 