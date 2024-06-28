from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class home(models.Model):
    name = models.CharField(max_length=20,null=True)
    faullname = models.CharField(max_length=20,null=True)
    phone = models.IntegerField(null=True)


    def __str__(self):
        return self.name