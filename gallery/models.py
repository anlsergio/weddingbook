from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=100, default='Image Title')
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='gallery_imgs')
    # thumbnail = models.ImageField(upload_to='gallery_imgs', null=True)
    likes = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     # During the original image saving
    #     # A copy of it will be saved being transformed to a lower size thumbnail
    #     img = Image.open(self.thumbnail.path)
    #     if img.height > 300 or img.width > 300:
    #         img = img.thumbnail(300, 300)
    #         img.save(self.thumbnail.path)

    def __str__(self):
        return self.title