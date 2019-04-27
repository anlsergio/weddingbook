import io
import mimetypes
import os

from django.conf import settings
from django.core.files.storage import default_storage as storage
from django.db import models
from django.urls import reverse
from PIL import Image as Image_PIL

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

        image = Image_PIL.open(self.image)
        if image.height > 600 or image.width > 600:
            image.thumbnail((600, 600), Image_PIL.ANTIALIAS)
            file_buffer = storage.open(self.image.name, "w")
            format = 'png'
            image.save(file_buffer, format)
            file_buffer.close()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('image_detail', kwargs={'pk': self.pk})
