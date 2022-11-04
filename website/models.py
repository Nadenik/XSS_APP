from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Module(models.Model):
    is_completed = models.BooleanField(default=False)
    challenge_completition = models.IntegerField(default=0)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def next_challenge_allowed(self, challenge_progress):
        if self.challenge_completition >= challenge_progress:
            return True
        else:
            return False

    class Meta:
        abstract = True

# I dont think it is wanted
# class Challenge(models.Model):
#     name = models.CharField(max_length=30)
#     is_completed = models.BooleanField(default=False)
#     module = models.ForeignKey(Module, on_delete=models.CASCADE)

class ReflectedXssModule(Module):
    name = models.CharField(max_length=30, default='reflected_xss')
    # progress in %
    def get_progress(self):
        xd = "{0:b}".format(self.challenge_completition).count("1")
        return int((xd/3)*100)

class DomBasedXssModule(Module):
    name = models.CharField(max_length=30, default='dom_based_xss')

class StoredXssModule(Module):
    name = models.CharField(max_length=30, default='stored_xss')