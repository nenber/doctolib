# Generated by Django 4.0.6 on 2022-07-05 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='slotEnd',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='slotStart',
            field=models.DateTimeField(),
        ),
    ]
