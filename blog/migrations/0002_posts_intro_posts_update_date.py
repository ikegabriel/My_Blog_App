# Generated by Django 4.0.5 on 2022-06-23 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='intro',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='update_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
