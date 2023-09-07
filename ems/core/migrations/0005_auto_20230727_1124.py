# Generated by Django 3.2.16 on 2023-07-27 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230722_1543'),
    ]

    operations = [
        migrations.DeleteModel(name='Machines'),
        migrations.CreateModel(
            'Machines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dop', models.DateField(blank=True, null=True, verbose_name='Date of Purcahse')),
                ('purchase_cost', models.FloatField(default=0)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('machine_spare', models.ManyToManyField(blank=True, related_name='machines', through='core.MachineSpares', to='core.Spares')),
                ('type_of_machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='typeOfMachine', to='core.equipment')),
            ],
        )
    ]