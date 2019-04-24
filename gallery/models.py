from django.db import models

from PIL import Image as Image_PIL

# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=100, default='Image Title')
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='gallery_imgs')
    # thumbnail = models.ImageField(upload_to='gallery_imgs', null=True)
    likes = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # During the original image saving
        # A copy of it will be saved being transformed to a lower size thumbnail
        #img = Image_PIL.open(self.image.path)
        #if img.height > 900 or img.width > 900:
        #    img = img.thumbnail(900, 900)
        #    img.save(self.image.path)

    def __str__(self):
        return self.title
