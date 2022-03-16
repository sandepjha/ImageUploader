from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.
class Image(models.Model):
    upload = models.ImageField(upload_to = "photos")
    date = models.DateTimeField(auto_now_add=True)
    