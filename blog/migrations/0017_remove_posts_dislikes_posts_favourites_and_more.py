# Generated by Django 4.0.5 on 2022-08-21 12:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0016_posts_dislikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='dislikes',
        ),
        migrations.AddField(
            model_name='posts',
            name='favourites',
            field=models.ManyToManyField(related_name='blog_favourites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='posts',
            name='header_image',
            field=models.ImageField(blank=True, default='static/blog/images/default.png', null=True, upload_to='images/%y%m%d'),
        ),
    ]