from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Module(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    challenge_completition = models.IntegerField(default=0)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)


class Challenge(models.Model):
    name = models.CharField(max_length=30)
    is_completed = models.BooleanField(default=False)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
