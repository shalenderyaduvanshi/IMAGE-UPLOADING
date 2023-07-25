from django.db import models


# Create your models here.
class ImageData(models.Model):
    objects = None
    Imagename = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='images_folder')

    class Meta:
        db_table = 'ImageData'
