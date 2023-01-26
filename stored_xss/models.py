from django.db import models
from website.models import StoredXssModule
from django.contrib.auth.models import User
from PIL import Image as Im
import PIL.ExifTags
# Create your models here.

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    stored_xss_module_related = models.ForeignKey(StoredXssModule, null=False, blank=False, on_delete=models.CASCADE)
    challenges = (
        ('1', 'level1'),
        ('2', 'level2')
    )
    challenge_assigned = models.CharField(choices=challenges, max_length=1, null=True)

    def __str__(self):
        return self.comment

        
class Image(models.Model):
    image = models.ImageField()
    description = models.TextField(null=True, blank=True)
    artist = models.CharField(blank=True, null=True, max_length=200)
    stored_xss_module_related = models.ForeignKey(StoredXssModule, null=False, blank=False, on_delete=models.CASCADE)
    
    # get exif author
    def exif(self):
        imagepath = self.image.path
        image = Im.open(imagepath)
        exifdata = image.getexif()
        if 315 in exifdata:
            return exifdata.get(315)
        

