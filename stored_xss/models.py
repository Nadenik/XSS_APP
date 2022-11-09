from django.db import models
from website.models import StoredXssModule
from django.contrib.auth.models import User
from PIL import Image as Im
from PIL.ExifTags import TAGS
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

class Image(models.Model):
    image = models.ImageField()
    stored_xss_module_related = models.ForeignKey(StoredXssModule, null=False, blank=False, on_delete=models.CASCADE)
        
    def exif(self):
        imagepath = self.image.path
        image = Im.open(imagepath)

        info_dict = {"Filename": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1)}

        for label,value in info_dict.items():
            print(f"{label:25}: {value}")
        exifdata = image.getexif()
        for tag_id in exifdata:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            # decode bytes 
            if isinstance(data, bytes):
                data = data.decode()
            print(f"{tag:25}: {data}")
        
