from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profesion = models.CharField(max_length=15)
    cui = models.IntegerField()
    file = models.FileField(default=None)

    def __str__(self):
        return f'{self.user.username} Profile'
