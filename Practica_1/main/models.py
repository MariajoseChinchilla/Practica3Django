from django.db import models
from django.shortcuts import render
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.views.generic import TemplateView

# Create your models here.

def get_upload_name(instance, filename):
    return f'archivos/p2/{instance.user.id}/{now().timestamp()}.p2'

class UploadedFiles(models.Model):
    title = models.CharField(max_length=100)
    p2 = models.FileField(upload_to=get_upload_name)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False, default=1)


    def __str__(self):
        return self.title

