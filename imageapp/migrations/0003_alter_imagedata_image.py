# Generated by Django 4.2.2 on 2023-06-08 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0002_alter_imagedata_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedata',
            name='Image',
            field=models.ImageField(upload_to='images_folder'),
        ),
    ]
