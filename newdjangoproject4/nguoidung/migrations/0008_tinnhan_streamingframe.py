# Generated by Django 3.1.7 on 2021-12-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nguoidung', '0007_auto_20211206_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='tinnhan',
            name='streamingFrame',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]