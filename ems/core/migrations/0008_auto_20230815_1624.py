# Generated by Django 3.2.16 on 2023-08-15 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_images_machineissue_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.RemoveField(
            model_name='machineissue',
            name='image',
        ),
        migrations.AddField(
            model_name='machineissue',
            name='image',
            field=models.ManyToManyField(blank=True, to='core.ImageModel'),
        ),
    ]