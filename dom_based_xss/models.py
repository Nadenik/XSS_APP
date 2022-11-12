from django.db import models
from website.models import DomBasedXssModule
# Create your models here.

class Text(models.Model):
    text = models.CharField(max_length=200)
    # every comments has an id of its related stored_xss_module
    dom_based_xss_module_related = models.ForeignKey(DomBasedXssModule, null=False, blank=False, on_delete=models.CASCADE)
    # challenges = (
    #     ('1', 'level1'),
    #     ('2', 'level2')
    # )
    # challenge_assigned = models.CharField(choices=challenges, max_length=1, null=True)

    def __str__(self):
        return self.text
