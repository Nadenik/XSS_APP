from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Module(models.Model):
    is_completed = models.BooleanField(default=False)
    challenge_completition = models.IntegerField(default=0)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        abstract = True

# I dont think it is wanted
# class Challenge(models.Model):
#     name = models.CharField(max_length=30)
#     is_completed = models.BooleanField(default=False)
#     module = models.ForeignKey(Module, on_delete=models.CASCADE)

class ReflectedXssModule(Module):
    name = models.CharField(max_length=30, default='reflected_xss')

class DomBasedXssModule(Module):
    name = models.CharField(max_length=30, default='dom_based_xss')
