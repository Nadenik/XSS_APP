from django.db import models
from website.models import StoredXssModule
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    # every comments has an id of its related stored_xss_module
    stored_xss_module_related = models.ForeignKey(StoredXssModule, null=False, blank=False, on_delete=models.CASCADE)
    challenges = (
        ('1', 'level1'),
        ('2', 'level2')
    )
    challenge_assigned = models.CharField(choices=challenges, max_length=1, null=True)

    def __str__(self):
        return self.comment
    # i need to seperate levels, 
