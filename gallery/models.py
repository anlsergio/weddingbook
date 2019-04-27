import io
import mimetypes
import os

from django.conf import settings
from django.core.files.storage import default_storage as storage
from django.db import models
from django.urls import reverse
from PIL import Image as Image_PIL

# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=100, default='Image Title')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             default=1, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='gallery_imgs')
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='image_likes')
    total_likes = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)


        # During the original image saving
        # A copy of it will be saved being transformed to a lower size thumbnail
        image = Image_PIL.open(self.image)
        image.thumbnail((600, 600), Image_PIL.ANTIALIAS)
        fh = storage.open(self.image.name, "w")
        format = 'png'  # You need to set the correct image format here
        image.save(fh, format)
        fh.close()
        # img = Image_PIL.open(storage.open(self.image.name))
        # print(img)
        # if img.height > 900 or img.width > 900:
        #    img = img.thumbnail((900, 900))
        #    print(img)
        #    img.save(self.image.path)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('image_detail', kwargs={'pk': self.pk})
