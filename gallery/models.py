from django.db import models
from django.conf import settings
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
        #img = Image_PIL.open(self.image.path)
        # if img.height > 900 or img.width > 900:
        #    img = img.thumbnail(900, 900)
        #    img.save(self.image.path)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('image_detail', kwargs={'pk': self.pk})
