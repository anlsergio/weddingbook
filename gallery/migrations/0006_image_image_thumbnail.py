# Generated by Django 2.1.8 on 2019-04-27 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_image_total_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_thumbnail',
            field=models.ImageField(default='default.png', upload_to='gallery_imgs'),
            preserve_default=False,
        ),
    ]
