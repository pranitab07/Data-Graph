from django.db import models

# Create your models here.
class files(models.Model):
    file_1=models.FileField(upload_to="NEW/",max_length=250,null=False)
